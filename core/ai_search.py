import os
import json
from groq import Groq


def ai_search(query: str, resources_qs):
    """
    Uses Groq API (free) to rank exam resources by relevance to the user's query.
    Falls back to basic ORM text search if API fails.
    """
    api_key = os.environ.get("GROQ_API_KEY")

    if not api_key:
        return _fallback_search(query, resources_qs)

    try:
        client = Groq(api_key=api_key)

        resources_data = list(resources_qs.values(
            'id', 'title', 'subject', 'difficulty', 'exam_type',
            'source_name', 'description', 'category__name'
        ))

        system_prompt = """You are an exam resource matching engine.
Given a user's search query and a list of exam resources, return a JSON array of resource IDs ranked by relevance.
Return ONLY a valid JSON array of integers (the IDs), nothing else. No explanation, no markdown, no preamble.
Maximum 10 results. If nothing is relevant, return an empty array: []"""

        user_message = f"""Query: {query}

Resources (JSON):
{json.dumps(resources_data, ensure_ascii=False)}

Return only a JSON array of IDs ranked by relevance to the query."""

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ],
            max_tokens=300,
            temperature=0.1
        )

        raw = response.choices[0].message.content.strip()
        raw = raw.replace("```json", "").replace("```", "").strip()
        id_list = json.loads(raw)

        if not isinstance(id_list, list):
            return _fallback_search(query, resources_qs)

        id_to_resource = {r.id: r for r in resources_qs}
        results = [id_to_resource[rid] for rid in id_list if rid in id_to_resource]
        return results

    except Exception:
        return _fallback_search(query, resources_qs)


def _fallback_search(query: str, resources_qs):
    """Basic text search fallback when Groq API is unavailable."""
    words = query.lower().split()
    from django.db.models import Q
    q_filter = Q()
    for word in words:
        q_filter |= Q(title__icontains=word)
        q_filter |= Q(description__icontains=word)
        q_filter |= Q(subject__icontains=word)
        q_filter |= Q(source_name__icontains=word)
        q_filter |= Q(category__name__icontains=word)
    return list(resources_qs.filter(q_filter).distinct()[:10])
