from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import ExamCategory, ExamResource


class Command(BaseCommand):
    help = 'Seed the database with exam categories and resources'

    def handle(self, *args, **kwargs):
        self.stdout.write('Clearing existing data...')
        ExamResource.objects.all().delete()
        ExamCategory.objects.all().delete()

        self.stdout.write('Creating categories...')
        categories = {}

        category_data = [
            # International
            ('SAT', 'sat', 'INTERNATIONAL', 'Scholastic Assessment Test for US college admissions'),
            ('ACT', 'act', 'INTERNATIONAL', 'American College Testing for US college admissions'),
            ('IELTS', 'ielts', 'INTERNATIONAL', 'International English Language Testing System'),
            ('TOEFL', 'toefl', 'INTERNATIONAL', 'Test of English as a Foreign Language'),
            ('Cambridge', 'cambridge', 'INTERNATIONAL', 'Cambridge English Qualifications (B2, C1, C2)'),
            ('GRE', 'gre', 'INTERNATIONAL', 'Graduate Record Examinations for graduate school'),
            ('GMAT', 'gmat', 'INTERNATIONAL', 'Graduate Management Admission Test for business school'),
            # Turkey
            ('YKS', 'yks', 'TURKEY', 'Yükseköğretim Kurumları Sınavı — Turkish university entrance'),
            ('TYT', 'tyt', 'TURKEY', 'Temel Yeterlilik Testi — basic competency test'),
            ('AYT', 'ayt', 'TURKEY', 'Alan Yeterlilik Testi — field competency test'),
            ('KPSS', 'kpss', 'TURKEY', 'Kamu Personeli Seçme Sınavı — civil service exam'),
            ('DGS', 'dgs', 'TURKEY', 'Dikey Geçiş Sınavı — vertical transfer exam'),
            ('ALES', 'ales', 'TURKEY', 'Akademik Lisansüstü Eğitim Sınavı — academic postgrad exam'),
        ]

        for name, slug, region, desc in category_data:
            cat = ExamCategory.objects.create(name=name, slug=slug, region=region, description=desc)
            categories[slug] = cat

        self.stdout.write('Creating resources...')
        resources = []

        sat = categories['sat']
        tyt = categories['tyt']
        ayt = categories['ayt']
        yks = categories['yks']

        # SAT (6)
        resources += [
            ExamResource(title='Khan Academy SAT Full Practice Test 1', category=sat,
                source_name='Khan Academy',
                url='https://www.khanacademy.org/test-prep/sat/x0a8c2e5f3af3d282:about-sat-suite/x0a8c2e5f3af3d282:full-length-sat-suite-practice-tests/a/full-length-sat-practice-tests',
                subject='General', difficulty='MEDIUM', exam_type='FULL_TEST',
                description='Free official SAT full-length practice tests on Khan Academy, developed in partnership with College Board.'),
            ExamResource(title='College Board SAT Practice Tests Download', category=sat,
                source_name='College Board',
                url='https://satsuite.collegeboard.org/sat/practice-preparation/practice-tests/linear',
                subject='General', difficulty='MEDIUM', exam_type='FULL_TEST',
                description='Official printable SAT practice tests directly from College Board. Download and print full-length tests with answer keys.'),
            ExamResource(title='SAT Digital Practice on Bluebook App', category=sat,
                source_name='College Board',
                url='https://satsuite.collegeboard.org/digital/digital-practice-preparation/practice-tests/bluebook',
                subject='General', difficulty='MEDIUM', exam_type='FULL_TEST',
                description='Take full-length digital SAT practice tests using the official Bluebook app from College Board.'),
            ExamResource(title='SAT Math Practice — Khan Academy', category=sat,
                source_name='Khan Academy',
                url='https://www.khanacademy.org/test-prep/sat/x0a8c2e5f3af3d282:digital-sat-math',
                subject='Math', difficulty='HARD', exam_type='SECTION',
                description='Comprehensive SAT Math practice on Khan Academy covering algebra, advanced math, problem solving and data analysis.'),
            ExamResource(title='SAT Reading and Writing — Khan Academy', category=sat,
                source_name='Khan Academy',
                url='https://www.khanacademy.org/test-prep/sat/x0a8c2e5f3af3d282:digital-sat-reading-and-writing',
                subject='Verbal', difficulty='MEDIUM', exam_type='SECTION',
                description='SAT Reading and Writing section practice with information and ideas, craft and structure, expression of ideas questions.'),
            ExamResource(title='Princeton Review Free SAT Practice Test', category=sat,
                source_name='Princeton Review',
                url='https://www.princetonreview.com/college/free-sat-practice-test',
                subject='General', difficulty='MEDIUM', exam_type='FULL_TEST',
                description='Free full-length SAT practice test from Princeton Review with detailed score analysis.'),
        ]

        # ACT (5)
        act = categories['act']
        resources += [
            ExamResource(title='ACT Official Free Practice Test PDF', category=act,
                source_name='ACT Official',
                url='https://www.act.org/content/dam/act/unsecured/documents/Preparing-for-the-ACT.pdf',
                subject='General', difficulty='MEDIUM', exam_type='FULL_TEST',
                description='Official free ACT practice test PDF with all four sections: English, Math, Reading, Science plus Writing.'),
            ExamResource(title='ACT Practice Test — Kaplan Free', category=act,
                source_name='Kaplan',
                url='https://www.kaptest.com/act/free/act-practice-test-options',
                subject='General', difficulty='MEDIUM', exam_type='FULL_TEST',
                description='Free ACT practice test from Kaplan with detailed score report and personalized feedback.'),
            ExamResource(title='ACT Math Practice Questions', category=act,
                source_name='Varsity Tutors',
                url='https://www.varsitytutors.com/act_math-practice-tests',
                subject='Math', difficulty='HARD', exam_type='SECTION',
                description='Hundreds of free ACT Math practice questions organized by topic and difficulty level.'),
            ExamResource(title='ACT English Practice Tests', category=act,
                source_name='Varsity Tutors',
                url='https://www.varsitytutors.com/act_english-practice-tests',
                subject='English', difficulty='MEDIUM', exam_type='SECTION',
                description='Free ACT English practice tests covering grammar, punctuation, sentence structure and rhetorical skills.'),
            ExamResource(title='ACT Reading Practice Tests', category=act,
                source_name='Varsity Tutors',
                url='https://www.varsitytutors.com/act_reading-practice-tests',
                subject='Reading', difficulty='MEDIUM', exam_type='SECTION',
                description='ACT Reading practice with prose fiction, social science, humanities and natural science passages.'),
        ]

        # IELTS (6)
        ielts = categories['ielts']
        resources += [
            ExamResource(title='IELTS Sample Test Questions — British Council', category=ielts,
                source_name='British Council',
                url='https://www.britishcouncil.org/exam/ielts/ielts-practice-materials/ielts-sample-test-questions',
                subject='General', difficulty='MEDIUM', exam_type='FULL_TEST',
                description='Official IELTS sample test questions from British Council covering all four skills: Listening, Reading, Writing, Speaking.'),
            ExamResource(title='IELTS Free Practice Tests — IDP', category=ielts,
                source_name='IDP IELTS',
                url='https://www.ielts.org/usa/ielts-for-test-takers/preparation/ielts-sample-test-questions',
                subject='General', difficulty='MEDIUM', exam_type='FULL_TEST',
                description='Free IELTS practice test questions from IDP, one of the three official IELTS partners.'),
            ExamResource(title='IELTS Academic Reading Practice', category=ielts,
                source_name='Road to IELTS',
                url='https://www.roadtoielts.com/practice-tests/reading/',
                subject='Reading', difficulty='HARD', exam_type='SECTION',
                description='IELTS Academic Reading practice tests with authentic passage types and question formats.'),
            ExamResource(title='IELTS Listening Practice Test — British Council', category=ielts,
                source_name='British Council',
                url='https://www.britishcouncil.org/exam/ielts/ielts-practice-materials/ielts-sample-test-questions/listen-sample',
                subject='Listening', difficulty='MEDIUM', exam_type='SECTION',
                description='Official IELTS Listening sample test with audio recordings from British Council.'),
            ExamResource(title='IELTS Writing Task 2 Sample Questions', category=ielts,
                source_name='IELTS.org',
                url='https://www.ielts.org/usa/ielts-for-test-takers/preparation/ielts-sample-test-questions/academic-writing',
                subject='Writing', difficulty='HARD', exam_type='SECTION',
                description='Official IELTS Academic Writing sample questions including Task 1 and Task 2 with band score descriptors.'),
            ExamResource(title='IELTS General Training Practice Test', category=ielts,
                source_name='British Council',
                url='https://www.britishcouncil.org/exam/ielts/ielts-practice-materials/ielts-sample-test-questions/general-training-reading',
                subject='Reading', difficulty='MEDIUM', exam_type='SECTION',
                description='Official IELTS General Training Reading sample test from British Council.'),
        ]

        # TOEFL (5)
        toefl = categories['toefl']
        resources += [
            ExamResource(title='TOEFL iBT Free Practice Test — ETS POWERPREP', category=toefl,
                source_name='ETS',
                url='https://www.ets.org/toefl/test-takers/ibt/prepare/powerprep.html',
                subject='General', difficulty='MEDIUM', exam_type='FULL_TEST',
                description='Free official TOEFL iBT practice test using ETS POWERPREP Online. Simulates the real test experience.'),
            ExamResource(title='TOEFL Sample Questions — ETS', category=toefl,
                source_name='ETS',
                url='https://www.ets.org/toefl/test-takers/ibt/prepare/tips-for-success/sample-questions.html',
                subject='General', difficulty='MEDIUM', exam_type='MINI_QUIZ',
                description='Official TOEFL iBT sample questions for all four sections from ETS with explanations.'),
            ExamResource(title='TOEFL Reading Practice — Magoosh', category=toefl,
                source_name='Magoosh',
                url='https://magoosh.com/toefl/toefl-reading-practice/',
                subject='Reading', difficulty='MEDIUM', exam_type='SECTION',
                description='Free TOEFL Reading practice passages and questions from Magoosh with detailed explanations.'),
            ExamResource(title='TOEFL Listening Practice — Magoosh', category=toefl,
                source_name='Magoosh',
                url='https://magoosh.com/toefl/toefl-listening-practice/',
                subject='Listening', difficulty='MEDIUM', exam_type='SECTION',
                description='Free TOEFL Listening practice with audio clips and questions from Magoosh.'),
            ExamResource(title='TOEFL Writing Practice Prompts — ETS', category=toefl,
                source_name='ETS',
                url='https://www.ets.org/toefl/test-takers/ibt/prepare/tips-for-success/independent-writing-topics.html',
                subject='Writing', difficulty='HARD', exam_type='SECTION',
                description='Official TOEFL Independent Writing practice topics from ETS with scoring rubrics.'),
        ]

        # GRE (5)
        gre = categories['gre']
        resources += [
            ExamResource(title='GRE POWERPREP Free Practice Test — ETS', category=gre,
                source_name='ETS',
                url='https://www.ets.org/gre/test-takers/general-test/prepare/powerprep.html',
                subject='General', difficulty='HARD', exam_type='FULL_TEST',
                description='Two free full-length GRE General Test practice exams from ETS using POWERPREP Online software.'),
            ExamResource(title='GRE Sample Questions — ETS Official', category=gre,
                source_name='ETS',
                url='https://www.ets.org/gre/test-takers/general-test/prepare/content/verbal-reasoning.html',
                subject='Verbal', difficulty='HARD', exam_type='SECTION',
                description='Official GRE Verbal Reasoning sample questions from ETS covering text completion, sentence equivalence and reading comprehension.'),
            ExamResource(title='GRE Quantitative Sample Questions — ETS', category=gre,
                source_name='ETS',
                url='https://www.ets.org/gre/test-takers/general-test/prepare/content/quantitative-reasoning.html',
                subject='Math', difficulty='HARD', exam_type='SECTION',
                description='Official GRE Quantitative Reasoning sample questions from ETS with explanations.'),
            ExamResource(title='GRE Analytical Writing Topics — ETS', category=gre,
                source_name='ETS',
                url='https://www.ets.org/gre/test-takers/general-test/prepare/analytical-writing-topics.html',
                subject='Writing', difficulty='HARD', exam_type='SECTION',
                description='Complete pool of GRE Analytical Writing practice topics published by ETS. Includes all Issue and Argument tasks.'),
            ExamResource(title='GRE Vocabulary Practice — Quizlet', category=gre,
                source_name='Quizlet',
                url='https://quizlet.com/gb/553311711/gre-high-frequency-words-flash-cards/',
                subject='Vocabulary', difficulty='MEDIUM', exam_type='MINI_QUIZ',
                description='High-frequency GRE vocabulary flashcards on Quizlet covering the most commonly tested words.'),
        ]

        # GMAT (4)
        gmat = categories['gmat']
        resources += [
            ExamResource(title='GMAT Official Free Practice Exam 1 — MBA.com', category=gmat,
                source_name='GMAC',
                url='https://www.mba.com/exam-prep/gmat-official-practice-exams-1-and-2',
                subject='General', difficulty='HARD', exam_type='FULL_TEST',
                description='Two free official GMAT practice exams from GMAC. Most authentic GMAT simulation available.'),
            ExamResource(title='GMAT Free Practice Questions — GMAC', category=gmat,
                source_name='GMAC',
                url='https://www.mba.com/exam-prep/gmat-official-practice-question-bank',
                subject='General', difficulty='HARD', exam_type='MINI_QUIZ',
                description='Free official GMAT practice questions from the GMAC question bank covering all tested areas.'),
            ExamResource(title='GMAT Quantitative Practice — Manhattan Prep', category=gmat,
                source_name='Manhattan Prep',
                url='https://www.manhattanprep.com/gmat/free-gmat-practice-test/',
                subject='Math', difficulty='HARD', exam_type='FULL_TEST',
                description='Free full-length GMAT practice test from Manhattan Prep with detailed score report.'),
            ExamResource(title='GMAT Verbal Practice Questions — Magoosh', category=gmat,
                source_name='Magoosh',
                url='https://gmat.magoosh.com/practices/start',
                subject='Verbal', difficulty='HARD', exam_type='SECTION',
                description='Free GMAT Verbal practice questions from Magoosh covering Critical Reasoning, Sentence Correction and Reading Comprehension.'),
        ]

        # Cambridge (4)
        cambridge = categories['cambridge']
        resources += [
            ExamResource(title='Cambridge B2 First Free Practice Test', category=cambridge,
                source_name='Cambridge English',
                url='https://www.cambridgeenglish.org/exams-and-tests/first/preparation/',
                subject='General', difficulty='MEDIUM', exam_type='FULL_TEST',
                description='Official Cambridge B2 First (FCE) free practice materials including sample papers with answer keys.'),
            ExamResource(title='Cambridge C1 Advanced Free Sample Papers', category=cambridge,
                source_name='Cambridge English',
                url='https://www.cambridgeenglish.org/exams-and-tests/advanced/preparation/',
                subject='General', difficulty='HARD', exam_type='FULL_TEST',
                description='Official Cambridge C1 Advanced (CAE) free sample papers for all components with answer keys.'),
            ExamResource(title='Cambridge C2 Proficiency Sample Papers', category=cambridge,
                source_name='Cambridge English',
                url='https://www.cambridgeenglish.org/exams-and-tests/proficiency/preparation/',
                subject='General', difficulty='HARD', exam_type='FULL_TEST',
                description='Official Cambridge C2 Proficiency (CPE) sample papers — the highest level Cambridge English qualification.'),
            ExamResource(title='Cambridge English Free Practice Activities', category=cambridge,
                source_name='Cambridge English',
                url='https://www.cambridgeenglish.org/learning-english/activities-for-learners/',
                subject='Grammar', difficulty='EASY', exam_type='MINI_QUIZ',
                description='Free interactive practice activities from Cambridge English for B1-C2 level learners.'),
        ]

        # YKS (5)
        resources += [
            ExamResource(title='YKS 2024 Tüm Sorular ve Cevaplar — ÖSYM', category=yks,
                source_name='ÖSYM',
                url='https://www.osym.gov.tr/TR,6552/2024-yks-tyt-ayt-ydt-soru-ve-cevaplari.html',
                subject='Genel', difficulty='MEDIUM', exam_type='FULL_TEST',
                description='2024 YKS sınavının tüm oturumlarına ait soru kitapçıkları ve cevap anahtarları ÖSYM tarafından yayınlandı.'),
            ExamResource(title='YKS 2023 Soru ve Cevapları — ÖSYM', category=yks,
                source_name='ÖSYM',
                url='https://www.osym.gov.tr/TR,6552/2023-yks-tyt-ayt-ydt-soru-ve-cevaplari.html',
                subject='Genel', difficulty='MEDIUM', exam_type='FULL_TEST',
                description='2023 YKS sınavının TYT ve AYT oturumlarına ait resmi soru kitapçıkları ve cevap anahtarları.'),
            ExamResource(title='TYT Deneme Sınavı — Doğru Tercih', category=yks,
                source_name='Doğru Tercih',
                url='https://www.dogrutercih.com/tyt-denemesi/',
                subject='Genel', difficulty='MEDIUM', exam_type='FULL_TEST',
                description='Ücretsiz online TYT deneme sınavı. Türkçe, Matematik, Fen Bilimleri ve Sosyal Bilimler sorularını içerir.'),
            ExamResource(title='AYT Matematik Soruları — Vitamin Eğitim', category=yks,
                source_name='Vitamin Eğitim',
                url='https://www.vitaminegitim.com/ayt-matematik',
                subject='Matematik', difficulty='HARD', exam_type='SECTION',
                description='AYT Matematik bölümü için konu bazlı sorular ve çözümlü örnekler.'),
            ExamResource(title='TYT Türkçe Soru Bankası — Sorubankası', category=yks,
                source_name='Sorubankası',
                url='https://www.sorubankasi.net/tyt-turkce',
                subject='Türkçe', difficulty='MEDIUM', exam_type='SECTION',
                description='TYT Türkçe için paragraf anlama, dil bilgisi ve anlam bilgisi soruları içeren ücretsiz soru bankası.'),
        ]

        # TYT (4)
        resources += [
            ExamResource(title='TYT 2024 Soru ve Cevapları — ÖSYM', category=tyt,
                source_name='ÖSYM',
                url='https://www.osym.gov.tr/TR,6552/2024-yks-tyt-ayt-ydt-soru-ve-cevaplari.html',
                subject='Genel', difficulty='MEDIUM', exam_type='FULL_TEST',
                description='2024 TYT sınavının resmi soru kitapçığı ve cevap anahtarı ÖSYM\'nin resmi sayfasında.'),
            ExamResource(title='TYT Matematik Online Test — Doğru Tercih', category=tyt,
                source_name='Doğru Tercih',
                url='https://www.dogrutercih.com/tyt-matematik/',
                subject='Matematik', difficulty='MEDIUM', exam_type='SECTION',
                description='TYT Matematik bölümü için ücretsiz online testler. Temel matematik ve problem çözme sorularını kapsar.'),
            ExamResource(title='TYT Fen Bilimleri Soruları', category=tyt,
                source_name='Fen Bilimleri',
                url='https://www.fenbilimleri.net/tyt-fen-bilimleri',
                subject='Fen Bilimleri', difficulty='MEDIUM', exam_type='SECTION',
                description='TYT Fen Bilimleri bölümü için Fizik, Kimya ve Biyoloji soruları ve çözümleri.'),
            ExamResource(title='TYT Sosyal Bilimler Soruları', category=tyt,
                source_name='Doğru Tercih',
                url='https://www.dogrutercih.com/tyt-sosyal/',
                subject='Sosyal Bilimler', difficulty='MEDIUM', exam_type='SECTION',
                description='TYT Sosyal Bilimler bölümü için Tarih, Coğrafya ve Felsefe soruları.'),
        ]

        # AYT (4)
        resources += [
            ExamResource(title='AYT 2024 Soru ve Cevapları — ÖSYM', category=ayt,
                source_name='ÖSYM',
                url='https://www.osym.gov.tr/TR,6552/2024-yks-tyt-ayt-ydt-soru-ve-cevaplari.html',
                subject='Genel', difficulty='HARD', exam_type='FULL_TEST',
                description='2024 AYT sınavının resmi soru kitapçığı ve cevap anahtarı. Matematik, Fen, Türk Dili ve Edebiyatı, Sosyal Bilimler oturumlarını kapsar.'),
            ExamResource(title='AYT Fizik Soruları — Fen Bilimleri', category=ayt,
                source_name='Fen Bilimleri',
                url='https://www.fenbilimleri.net/ayt-fizik',
                subject='Fizik', difficulty='HARD', exam_type='SECTION',
                description='AYT Fizik bölümü için konu bazlı sorular. Mekanik, elektrik, dalgalar ve modern fizik konularını kapsar.'),
            ExamResource(title='AYT Kimya Soruları — Fen Bilimleri', category=ayt,
                source_name='Fen Bilimleri',
                url='https://www.fenbilimleri.net/ayt-kimya',
                subject='Kimya', difficulty='HARD', exam_type='SECTION',
                description='AYT Kimya bölümü için organik kimya, mol kavramı ve kimyasal denge soruları.'),
            ExamResource(title='AYT Türk Dili ve Edebiyatı — ÖSYM Arşiv', category=ayt,
                source_name='ÖSYM',
                url='https://www.osym.gov.tr/TR,6552/2024-yks-tyt-ayt-ydt-soru-ve-cevaplari.html',
                subject='Edebiyat', difficulty='HARD', exam_type='SECTION',
                description='AYT Türk Dili ve Edebiyatı oturumu soru ve cevapları ÖSYM resmi arşivinden.'),
        ]

        # KPSS (4)
        kpss = categories['kpss']
        resources += [
            ExamResource(title='KPSS 2024 Soru ve Cevapları — ÖSYM', category=kpss,
                source_name='ÖSYM',
                url='https://www.osym.gov.tr/TR,6552/kpss.html',
                subject='Genel Yetenek', difficulty='MEDIUM', exam_type='FULL_TEST',
                description='2024 KPSS Genel Yetenek ve Genel Kültür sınavının resmi soru kitapçıkları ve cevap anahtarları.'),
            ExamResource(title='KPSS Matematik Soruları — Doğru Tercih', category=kpss,
                source_name='Doğru Tercih',
                url='https://www.dogrutercih.com/kpss-matematik/',
                subject='Matematik', difficulty='MEDIUM', exam_type='SECTION',
                description='KPSS Matematik için sayısal yetenek ve problem çözme soruları. Konu bazlı pratik testler.'),
            ExamResource(title='KPSS Türkçe Soruları — Doğru Tercih', category=kpss,
                source_name='Doğru Tercih',
                url='https://www.dogrutercih.com/kpss-turkce/',
                subject='Türkçe', difficulty='MEDIUM', exam_type='SECTION',
                description='KPSS Türkçe için paragraf anlama, dil bilgisi ve anlam bilgisi soruları.'),
            ExamResource(title='KPSS Tarih Soruları — Doğru Tercih', category=kpss,
                source_name='Doğru Tercih',
                url='https://www.dogrutercih.com/kpss-tarih/',
                subject='Tarih', difficulty='MEDIUM', exam_type='SECTION',
                description='KPSS Genel Kültür Tarih bölümü için Osmanlı ve Cumhuriyet dönemi soruları.'),
        ]

        # DGS (3)
        dgs = categories['dgs']
        resources += [
            ExamResource(title='DGS 2024 Soru ve Cevapları — ÖSYM', category=dgs,
                source_name='ÖSYM',
                url='https://www.osym.gov.tr/TR,6552/dgs.html',
                subject='Genel', difficulty='MEDIUM', exam_type='FULL_TEST',
                description='2024 DGS sınavının resmi soru kitapçığı ve cevap anahtarı ÖSYM tarafından yayınlandı.'),
            ExamResource(title='DGS Sayısal Bölüm Soruları', category=dgs,
                source_name='Doğru Tercih',
                url='https://www.dogrutercih.com/dgs-sayisal/',
                subject='Sayısal', difficulty='MEDIUM', exam_type='SECTION',
                description='DGS Sayısal bölümü için matematik ve fen bilimleri soruları ve çözümleri.'),
            ExamResource(title='DGS Sözel Bölüm Soruları', category=dgs,
                source_name='Doğru Tercih',
                url='https://www.dogrutercih.com/dgs-sozel/',
                subject='Sözel', difficulty='MEDIUM', exam_type='SECTION',
                description='DGS Sözel bölümü için Türkçe ve sosyal bilimler soruları.'),
        ]

        # ALES (4)
        ales = categories['ales']
        resources += [
            ExamResource(title='ALES 2024 Soru ve Cevapları — ÖSYM', category=ales,
                source_name='ÖSYM',
                url='https://www.osym.gov.tr/TR,6552/ales.html',
                subject='Genel', difficulty='HARD', exam_type='FULL_TEST',
                description='2024 ALES sınavının resmi soru kitapçıkları ve cevap anahtarları ÖSYM resmi sitesinde.'),
            ExamResource(title='ALES Sayısal Bölüm Soruları — Doğru Tercih', category=ales,
                source_name='Doğru Tercih',
                url='https://www.dogrutercih.com/ales-sayisal/',
                subject='Sayısal', difficulty='HARD', exam_type='SECTION',
                description='ALES Sayısal bölümü için ileri düzey matematik soruları ve ayrıntılı çözümleri.'),
            ExamResource(title='ALES Sözel Bölüm Soruları — Doğru Tercih', category=ales,
                source_name='Doğru Tercih',
                url='https://www.dogrutercih.com/ales-sozel/',
                subject='Sözel', difficulty='MEDIUM', exam_type='SECTION',
                description='ALES Sözel bölümü için kelime anlamı, paragraf ve dil bilgisi soruları.'),
            ExamResource(title='ALES Deneme Sınavı — Online', category=ales,
                source_name='Doğru Tercih',
                url='https://www.dogrutercih.com/ales-denemesi/',
                subject='Genel', difficulty='HARD', exam_type='FULL_TEST',
                description='Ücretsiz online ALES deneme sınavı. Sayısal ve sözel bölümlerin tamamını kapsar.'),
        ]

        ExamResource.objects.bulk_create(resources)

        # Create users
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@examfind.com', 'admin123')

        for username, email in [('student1', 'student1@example.com'), ('student2', 'student2@example.com')]:
            if not User.objects.filter(username=username).exists():
                user = User.objects.create_user(username, email, 'pass123')
                user.first_name = username.capitalize()
                user.save()

        total = ExamResource.objects.count()
        self.stdout.write(self.style.SUCCESS(
            f'Seeded successfully! {total} resources created across {ExamCategory.objects.count()} categories.'
        ))
