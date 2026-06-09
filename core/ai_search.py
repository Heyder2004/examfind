import os  # Bu projenin en önemli dosyası. Normal arama 'bu kelime var mı yok mu' diye bakar. Ben bunun yerine yapay zekaya soruyorum:
import json
from groq import Groq
from ddgs import DDGS

# Trusted exam resource domains — used to boost credibility scoring
TRUSTED_DOMAINS = [
    'khanacademy.org',
    'collegeboard.org',
    'ets.org',
    'act.org',
    'ielts.org',
    'britishcouncil.org',
    'cambridgeenglish.org',
    'idp.com',
    'magoosh.com',
    'kaptest.com',
    'princetonreview.com',
    'manhattanprep.com',
    'mba.com',
    'gmac.com',
    'varsitytutors.com',
    'quizlet.com',
    'osym.gov.tr',
    'yoksis.yok.gov.tr',
    'dogrutercih.com',
    'vitaminegitim.com',
    'prepscholar.com',
    'roadtoielts.com',
]

def refine_query_with_groq(query: str) -> str:
    """
    Uses Groq to refine the user's natural language query into
    an optimized web search string for finding free exam practice tests.
    """
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        return query + " free practice test"

    try:
        client = Groq(api_key=api_key)
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": """You are a search query optimizer for an exam practice test finder.
Given a user's natural language query, return ONLY an optimized web search string that will find free practice tests.
Rules:
- Always add "free practice test" if not present
- Keep it concise (max 10 words)
- Return ONLY the search query string, nothing else, no quotes, no explanation"""
                },
                {
                    "role": "user",
                    "content": f"User query: {query}"
                }
            ],
            max_tokens=50,
            temperature=0.1
        )
        refined = response.choices[0].message.content.strip()
        refined = refined.strip('"\'')
        return refined
    except Exception:
        return query + " free practice test"


def search_duckduckgo_html(query: str) -> list:
    """
    Searches DuckDuckGo via the ddgs library (handles bot-detection internally).
    Returns a list of dicts with: title, url, description, source
    """
    try:
        raw = list(DDGS().text(query, max_results=10))
        results = []
        for item in raw:
            url = item.get('href', '')
            title = item.get('title', '')
            description = item.get('body', '')
            if url and title:
                results.append({
                    'title': title,
                    'url': url,
                    'description': description,
                    'source': extract_domain(url)
                })
        return results
    except Exception:
        return []


def extract_domain(url: str) -> str:
    """Extracts clean domain name from URL."""
    try:
        from urllib.parse import urlparse
        parsed = urlparse(url)
        domain = parsed.netloc.replace('www.', '')
        return domain
    except Exception:
        return url


def is_trusted_domain(url: str) -> bool:
    """Check if URL is from a trusted exam resource domain."""
    domain = extract_domain(url).lower()
    return any(trusted in domain for trusted in TRUSTED_DOMAINS)


def score_result(result: dict) -> int:
    """Score a result by credibility. Higher = better."""
    score = 0
    url = result.get('url', '').lower()
    title = result.get('title', '').lower()
    desc = result.get('description', '').lower()

    if is_trusted_domain(url):
        score += 10

    good_keywords = ['practice test', 'practice exam', 'free test', 'sample test',
                     'mock test', 'quiz', 'questions', 'preparation', 'prep']
    for kw in good_keywords:
        if kw in title or kw in desc:
            score += 2

    bad_patterns = ['reddit.com', 'youtube.com', 'twitter.com', 'facebook.com',
                    'instagram.com', 'pinterest.com', 'amazon.com']
    for bad in bad_patterns:
        if bad in url:
            score -= 5

    return score


def live_search(query: str) -> list:
    """
    Main search function. Refines query with Groq, searches DuckDuckGo,
    scores and returns ranked results.
    """
    refined_query = refine_query_with_groq(query)

    results = search_duckduckgo_html(refined_query)

    seen_urls = set()
    unique_results = []
    for r in results:
        if r['url'] not in seen_urls:
            seen_urls.add(r['url'])
            unique_results.append(r)

    for r in unique_results:
        r['score'] = score_result(r)
        r['is_trusted'] = is_trusted_domain(r['url'])

    unique_results.sort(key=lambda x: x['score'], reverse=True)

    return unique_results[:10]
