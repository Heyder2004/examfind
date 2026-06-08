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

        # SAT (6)
        sat = categories['sat']
        resources += [
            ExamResource(title='Khan Academy SAT Full Practice Test', category=sat, source_name='Khan Academy',
                url='https://www.khanacademy.org/test-prep/sat', subject='General', difficulty='MEDIUM',
                exam_type='FULL_TEST', description='Free official SAT practice tests on Khan Academy, developed in partnership with College Board. Includes full-length tests with detailed answer explanations.'),
            ExamResource(title='College Board Official SAT Practice Test 1', category=sat, source_name='College Board',
                url='https://satsuite.collegeboard.org/sat/practice-preparation/practice-tests', subject='General', difficulty='MEDIUM',
                exam_type='FULL_TEST', description='Official SAT practice tests directly from College Board. The most authentic SAT preparation available.'),
            ExamResource(title='SAT Math Section Practice — Hard Level', category=sat, source_name='Khan Academy',
                url='https://www.khanacademy.org/test-prep/sat/x0a8c2e5f3af3d282:digital-sat-math', subject='Math', difficulty='HARD',
                exam_type='SECTION', description='Advanced SAT Math practice targeting the most challenging question types including advanced algebra and problem solving.'),
            ExamResource(title='SAT Reading and Writing Practice', category=sat, source_name='Khan Academy',
                url='https://www.khanacademy.org/test-prep/sat/x0a8c2e5f3af3d282:digital-sat-reading-and-writing', subject='Verbal', difficulty='MEDIUM',
                exam_type='SECTION', description='Comprehensive SAT Reading and Writing section practice with detailed explanations for every question.'),
            ExamResource(title='Princeton Review SAT Practice Test', category=sat, source_name='Princeton Review',
                url='https://www.princetonreview.com/college/free-sat-practice-test', subject='General', difficulty='MEDIUM',
                exam_type='FULL_TEST', description='Free full-length SAT practice test from Princeton Review with score analysis and detailed performance breakdown.'),
            ExamResource(title='SAT Math Easy Practice Quiz', category=sat, source_name='Khan Academy',
                url='https://www.khanacademy.org/test-prep/sat', subject='Math', difficulty='EASY',
                exam_type='MINI_QUIZ', description='Beginner-friendly SAT Math practice covering fundamental algebra, geometry, and data analysis skills.'),
        ]

        # ACT (5)
        act = categories['act']
        resources += [
            ExamResource(title='ACT Official Free Practice Test', category=act, source_name='ACT Official',
                url='https://www.act.org/content/act/en/products-and-services/the-act/test-preparation/free-act-test-prep.html',
                subject='General', difficulty='MEDIUM', exam_type='FULL_TEST',
                description='Official free ACT practice test with answer key and scoring guide directly from ACT.org.'),
            ExamResource(title='ACT English Section Practice', category=act, source_name='Kaplan',
                url='https://www.kaptest.com/act/free/act-practice-test-options', subject='English', difficulty='MEDIUM',
                exam_type='SECTION', description='Targeted ACT English practice covering grammar, punctuation, and rhetorical skills.'),
            ExamResource(title='ACT Math Practice Test', category=act, source_name='Kaplan',
                url='https://www.kaptest.com/act/free/act-practice-test-options', subject='Math', difficulty='HARD',
                exam_type='SECTION', description='Challenging ACT Math practice covering pre-algebra through trigonometry.'),
            ExamResource(title='ACT Science Reasoning Practice', category=act, source_name='PrepScholar',
                url='https://blog.prepscholar.com/act-science-practice-tests', subject='Science', difficulty='MEDIUM',
                exam_type='SECTION', description='ACT Science section practice focusing on data interpretation, research summaries, and conflicting viewpoints.'),
            ExamResource(title='ACT Reading Comprehension Mini Quiz', category=act, source_name='Varsity Tutors',
                url='https://www.varsitytutors.com/act_reading-practice-tests', subject='Reading', difficulty='EASY',
                exam_type='MINI_QUIZ', description='Quick ACT Reading practice quizzes targeting prose fiction, social science, humanities, and natural science passages.'),
        ]

        # IELTS (6)
        ielts = categories['ielts']
        resources += [
            ExamResource(title='British Council IELTS Academic Practice Test', category=ielts, source_name='British Council',
                url='https://www.britishcouncil.org/exam/ielts/ielts-practice-materials', subject='General', difficulty='MEDIUM',
                exam_type='FULL_TEST', description='Official IELTS practice materials from British Council, one of the three co-owners of IELTS.'),
            ExamResource(title='IELTS Reading Academic Practice', category=ielts, source_name='IDP IELTS',
                url='https://www.ielts.org/about-ielts/ielts-for-test-takers/preparation', subject='Reading', difficulty='HARD',
                exam_type='SECTION', description='Official IELTS Academic Reading practice tests with detailed answer keys and band score guidance.'),
            ExamResource(title='IELTS Listening Practice Test', category=ielts, source_name='British Council',
                url='https://www.britishcouncil.org/exam/ielts/ielts-practice-materials', subject='Listening', difficulty='MEDIUM',
                exam_type='SECTION', description='Full IELTS Listening section practice with audio recordings and answer sheets.'),
            ExamResource(title='IELTS Writing Task 2 Practice', category=ielts, source_name='IELTS.org',
                url='https://www.ielts.org/about-ielts/ielts-for-test-takers/preparation', subject='Writing', difficulty='HARD',
                exam_type='SECTION', description='IELTS Academic Writing Task 2 essay practice with sample answers and examiner comments.'),
            ExamResource(title='IELTS General Training Practice Test', category=ielts, source_name='IDP IELTS',
                url='https://www.ielts.org/about-ielts/ielts-for-test-takers/preparation', subject='General', difficulty='MEDIUM',
                exam_type='FULL_TEST', description='Complete IELTS General Training practice test for those applying for migration or secondary education.'),
            ExamResource(title='IELTS Speaking Practice Topics', category=ielts, source_name='British Council',
                url='https://www.britishcouncil.org/exam/ielts/ielts-practice-materials', subject='Speaking', difficulty='MEDIUM',
                exam_type='SECTION', description='Common IELTS Speaking part 1, 2, and 3 topics with model answers and examiner tips.'),
        ]

        # TOEFL (5)
        toefl = categories['toefl']
        resources += [
            ExamResource(title='ETS TOEFL iBT Free Practice Test', category=toefl, source_name='ETS',
                url='https://www.ets.org/toefl/test-takers/ibt/prepare/powerprep.html', subject='General', difficulty='MEDIUM',
                exam_type='FULL_TEST', description='Official TOEFL iBT practice test from ETS using the real POWERPREP software.'),
            ExamResource(title='TOEFL Reading Section Practice', category=toefl, source_name='Magoosh',
                url='https://magoosh.com/toefl/free-toefl-practice-tests/', subject='Reading', difficulty='MEDIUM',
                exam_type='SECTION', description='Free TOEFL Reading practice passages with detailed explanations from Magoosh.'),
            ExamResource(title='TOEFL Listening Practice', category=toefl, source_name='ETS',
                url='https://www.ets.org/toefl/test-takers/ibt/prepare.html', subject='Listening', difficulty='MEDIUM',
                exam_type='SECTION', description='Official TOEFL Listening practice with academic lectures and conversations.'),
            ExamResource(title='TOEFL Writing Practice Prompts', category=toefl, source_name='Magoosh',
                url='https://magoosh.com/toefl/free-toefl-practice-tests/', subject='Writing', difficulty='HARD',
                exam_type='SECTION', description='TOEFL integrated and independent writing task practice with sample scored responses.'),
            ExamResource(title='TOEFL Vocabulary Mini Quiz', category=toefl, source_name='Vocabulary.com',
                url='https://www.vocabulary.com/lists/toefl', subject='Vocabulary', difficulty='EASY',
                exam_type='MINI_QUIZ', description='Essential TOEFL vocabulary practice targeting the most commonly tested academic words.'),
        ]

        # GRE (5)
        gre = categories['gre']
        resources += [
            ExamResource(title='ETS GRE POWERPREP Practice Test 1', category=gre, source_name='ETS',
                url='https://www.ets.org/gre/test-takers/general-test/prepare/powerprep.html', subject='General', difficulty='MEDIUM',
                exam_type='FULL_TEST', description='Free official GRE General Test practice test using ETS POWERPREP software. Most authentic GRE simulation available.'),
            ExamResource(title='GRE Verbal Reasoning Practice', category=gre, source_name='Manhattan Prep',
                url='https://www.manhattanprep.com/gre/free-gre-practice-test/', subject='Verbal', difficulty='HARD',
                exam_type='SECTION', description='Challenging GRE Verbal Reasoning practice covering text completion, sentence equivalence, and reading comprehension.'),
            ExamResource(title='GRE Quantitative Reasoning Practice', category=gre, source_name='ETS',
                url='https://www.ets.org/gre/test-takers/general-test/prepare/powerprep.html', subject='Math', difficulty='HARD',
                exam_type='SECTION', description='Official GRE Quantitative Reasoning practice with arithmetic, algebra, geometry, and data analysis.'),
            ExamResource(title='GRE Analytical Writing Practice', category=gre, source_name='ETS',
                url='https://www.ets.org/gre/test-takers/general-test/prepare/analytical-writing-topics.html', subject='Writing', difficulty='HARD',
                exam_type='SECTION', description='Official GRE Analytical Writing practice prompts with scored sample responses and rater commentary.'),
            ExamResource(title='GRE Vocabulary Flashcards', category=gre, source_name='Quizlet',
                url='https://quizlet.com/subject/gre-vocabulary/', subject='Vocabulary', difficulty='MEDIUM',
                exam_type='MINI_QUIZ', description='Popular GRE vocabulary sets on Quizlet covering high-frequency GRE words with definitions and example sentences.'),
        ]

        # GMAT (4)
        gmat = categories['gmat']
        resources += [
            ExamResource(title='GMAC Official GMAT Practice Exam 1 & 2', category=gmat, source_name='GMAC',
                url='https://www.mba.com/exam-prep/gmat-official-practice-exams-1-and-2', subject='General', difficulty='HARD',
                exam_type='FULL_TEST', description='Official free GMAT practice exams from GMAC. The most authentic GMAT preparation available.'),
            ExamResource(title='GMAT Quantitative Practice', category=gmat, source_name='Magoosh',
                url='https://gmat.magoosh.com/', subject='Math', difficulty='HARD',
                exam_type='SECTION', description='Free GMAT Quantitative Reasoning practice covering problem solving and data sufficiency.'),
            ExamResource(title='GMAT Verbal Critical Reasoning', category=gmat, source_name='Manhattan Prep',
                url='https://www.manhattanprep.com/gmat/free-gmat-practice-test/', subject='Verbal', difficulty='HARD',
                exam_type='SECTION', description='GMAT Critical Reasoning practice targeting argument analysis, assumption identification, and logical flaw detection.'),
            ExamResource(title='GMAT Data Insights Practice', category=gmat, source_name='GMAC',
                url='https://www.mba.com/exam-prep', subject='Data Analysis', difficulty='MEDIUM',
                exam_type='SECTION', description='Practice for the GMAT Focus Edition Data Insights section covering data sufficiency and multi-source reasoning.'),
        ]

        # Cambridge (4)
        cambridge = categories['cambridge']
        resources += [
            ExamResource(title='Cambridge B2 First Free Practice Test', category=cambridge, source_name='Cambridge English',
                url='https://www.cambridgeenglish.org/exams-and-tests/first/preparation/', subject='General', difficulty='MEDIUM',
                exam_type='FULL_TEST', description='Free Cambridge B2 First (FCE) practice test with answer keys from Cambridge Assessment English.'),
            ExamResource(title='Cambridge C1 Advanced Practice Materials', category=cambridge, source_name='Cambridge English',
                url='https://www.cambridgeenglish.org/exams-and-tests/advanced/preparation/', subject='General', difficulty='HARD',
                exam_type='FULL_TEST', description='Official Cambridge C1 Advanced (CAE) practice tests including reading, writing, listening, and speaking components.'),
            ExamResource(title='Cambridge C2 Proficiency Sample Papers', category=cambridge, source_name='Cambridge English',
                url='https://www.cambridgeenglish.org/exams-and-tests/proficiency/preparation/', subject='General', difficulty='HARD',
                exam_type='FULL_TEST', description='Cambridge C2 Proficiency (CPE) sample papers for the highest level Cambridge English qualification.'),
            ExamResource(title='Cambridge English Grammar in Use Quiz', category=cambridge, source_name='Cambridge English',
                url='https://www.cambridgeenglish.org/learning-english/activities-for-learners/', subject='Grammar', difficulty='EASY',
                exam_type='MINI_QUIZ', description='Interactive grammar quizzes from Cambridge English for learners at B1-C2 levels.'),
        ]

        # YKS (5) — using yks category for both YKS and TYT/AYT resources
        yks = categories['yks']
        tyt = categories['tyt']
        ayt = categories['ayt']
        resources += [
            ExamResource(title='ÖSYM YKS 2024 Örnek Soruları', category=yks, source_name='ÖSYM',
                url='https://www.osym.gov.tr/TR,6552/2024-yks.html', subject='Genel', difficulty='MEDIUM',
                exam_type='FULL_TEST', description='ÖSYM tarafından yayınlanan resmi YKS örnek soruları ve cevap anahtarları.'),
            ExamResource(title='TYT Türkçe Soru Bankası', category=tyt, source_name='Fen Bilimleri Yayınları',
                url='https://www.osym.gov.tr', subject='Türkçe', difficulty='MEDIUM',
                exam_type='SECTION', description='TYT Türkçe bölümü için paragraf, dil bilgisi ve anlam bilgisi soruları.'),
            ExamResource(title='AYT Matematik Deneme Sınavı', category=ayt, source_name='ÖSYM',
                url='https://www.osym.gov.tr', subject='Matematik', difficulty='HARD',
                exam_type='FULL_TEST', description='AYT Matematik bölümü için kapsamlı deneme sınavı soruları.'),
            ExamResource(title='TYT Matematik Temel Sorular', category=tyt, source_name='Vitamin Eğitim',
                url='https://www.vitaminegitim.com', subject='Matematik', difficulty='EASY',
                exam_type='SECTION', description='TYT Matematik için temel seviye pratik sorular. Başlangıç düzeyindeki öğrenciler için idealdir.'),
            ExamResource(title='AYT Türk Dili ve Edebiyatı', category=ayt, source_name='ÖSYM',
                url='https://www.osym.gov.tr', subject='Edebiyat', difficulty='HARD',
                exam_type='SECTION', description='AYT Türk Dili ve Edebiyatı bölümü örnek soruları ve konu anlatımları.'),
        ]

        # KPSS (3)
        kpss = categories['kpss']
        resources += [
            ExamResource(title='KPSS Genel Yetenek-Genel Kültür Deneme', category=kpss, source_name='ÖSYM',
                url='https://www.osym.gov.tr', subject='Genel Yetenek', difficulty='MEDIUM',
                exam_type='FULL_TEST', description='KPSS Genel Yetenek ve Genel Kültür bölümleri için resmi örnek sorular.'),
            ExamResource(title='KPSS Eğitim Bilimleri Soruları', category=kpss, source_name='ÖSYM',
                url='https://www.osym.gov.tr', subject='Eğitim Bilimleri', difficulty='HARD',
                exam_type='SECTION', description='KPSS Eğitim Bilimleri (öğretmen adayları) için örnek sorular ve konu özetleri.'),
            ExamResource(title='KPSS Türkçe Mini Quiz', category=kpss, source_name='Doğru Tercih',
                url='https://www.dogrutercih.com', subject='Türkçe', difficulty='EASY',
                exam_type='MINI_QUIZ', description='KPSS Türkçe için kısa pratik sorular. Kelime bilgisi, dil bilgisi ve anlama sorularını kapsar.'),
        ]

        # ALES (3)
        ales = categories['ales']
        resources += [
            ExamResource(title='ALES Sayısal Bölüm Örnek Soruları', category=ales, source_name='ÖSYM',
                url='https://www.osym.gov.tr', subject='Sayısal', difficulty='HARD',
                exam_type='SECTION', description='ALES Sayısal bölümü için ÖSYM tarafından yayınlanan örnek sorular.'),
            ExamResource(title='ALES Sözel Bölüm Deneme', category=ales, source_name='ÖSYM',
                url='https://www.osym.gov.tr', subject='Sözel', difficulty='MEDIUM',
                exam_type='SECTION', description='ALES Sözel bölümü örnek soruları, kelime anlamı ve paragraf sorularını içerir.'),
            ExamResource(title='ALES Tam Deneme Sınavı', category=ales, source_name='ÖSYM',
                url='https://www.osym.gov.tr', subject='Genel', difficulty='HARD',
                exam_type='FULL_TEST', description='ALES için tam uzunlukta deneme sınavı. Sayısal ve sözel bölümlerin tamamını kapsar.'),
        ]

        # DGS (2)
        dgs = categories['dgs']
        resources += [
            ExamResource(title='DGS Sayısal Örnek Sorular', category=dgs, source_name='ÖSYM',
                url='https://www.osym.gov.tr', subject='Sayısal', difficulty='MEDIUM',
                exam_type='SECTION', description='DGS sınavı sayısal bölümü için resmi örnek sorular ve çözümleri.'),
            ExamResource(title='DGS Sözel Örnek Sorular', category=dgs, source_name='ÖSYM',
                url='https://www.osym.gov.tr', subject='Sözel', difficulty='MEDIUM',
                exam_type='SECTION', description='DGS sınavı sözel bölümü için resmi örnek sorular ve çözümleri.'),
        ]

        # Extra resources to reach 60+
        resources += [
            ExamResource(title='SAT Writing & Language Practice Quiz', category=sat, source_name='PrepScholar',
                url='https://blog.prepscholar.com/free-sat-practice-tests', subject='Writing', difficulty='MEDIUM',
                exam_type='MINI_QUIZ', description='Targeted SAT Writing and Language practice with grammar rules and editing strategies.'),
            ExamResource(title='SAT Evidence-Based Reading Practice', category=sat, source_name='Varsity Tutors',
                url='https://www.varsitytutors.com/sat_reading-practice-tests', subject='Reading', difficulty='HARD',
                exam_type='SECTION', description='Advanced SAT Reading practice with complex passages and evidence-based questions.'),
            ExamResource(title='ACT Full Practice Test 2024', category=act, source_name='PrepScholar',
                url='https://blog.prepscholar.com/free-complete-official-act-practice-tests', subject='General', difficulty='MEDIUM',
                exam_type='FULL_TEST', description='Recent ACT full practice test with all four sections: English, Math, Reading, and Science.'),
            ExamResource(title='IELTS Academic Writing Task 1', category=ielts, source_name='IELTS.org',
                url='https://www.ielts.org/about-ielts/ielts-for-test-takers/preparation', subject='Writing', difficulty='MEDIUM',
                exam_type='SECTION', description='IELTS Academic Writing Task 1 practice: describing charts, graphs, maps, and diagrams.'),
            ExamResource(title='TOEFL Speaking Practice Questions', category=toefl, source_name='ETS',
                url='https://www.ets.org/toefl/test-takers/ibt/prepare.html', subject='Speaking', difficulty='MEDIUM',
                exam_type='SECTION', description='Official TOEFL Speaking practice questions with sample responses and scoring rubrics.'),
            ExamResource(title='GRE Issue Essay Practice Prompts', category=gre, source_name='ETS',
                url='https://www.ets.org/gre/test-takers/general-test/prepare/analytical-writing-topics.html', subject='Writing', difficulty='HARD',
                exam_type='SECTION', description='Complete pool of GRE Issue essay prompts from ETS with scoring guides.'),
            ExamResource(title='Cambridge B1 Preliminary Practice Test', category=cambridge, source_name='Cambridge English',
                url='https://www.cambridgeenglish.org/exams-and-tests/preliminary/preparation/', subject='General', difficulty='EASY',
                exam_type='FULL_TEST', description='Free Cambridge B1 Preliminary (PET) practice test with answer keys.'),
            ExamResource(title='YKS Fen Bilimleri Deneme', category=yks, source_name='ÖSYM',
                url='https://www.osym.gov.tr', subject='Fen Bilimleri', difficulty='HARD',
                exam_type='SECTION', description='YKS Fen Bilimleri (Fizik, Kimya, Biyoloji) bölümü için örnek sorular.'),
            ExamResource(title='TYT Sosyal Bilimler Soruları', category=tyt, source_name='ÖSYM',
                url='https://www.osym.gov.tr', subject='Sosyal Bilimler', difficulty='MEDIUM',
                exam_type='SECTION', description='TYT Sosyal Bilimler bölümü için Tarih, Coğrafya ve Felsefe soruları.'),
            ExamResource(title='KPSS Genel Kültür Deneme', category=kpss, source_name='ÖSYM',
                url='https://www.osym.gov.tr', subject='Genel Kültür', difficulty='MEDIUM',
                exam_type='SECTION', description='KPSS Genel Kültür soruları: Tarih, Coğrafya, Vatandaşlık ve Güncel bilgiler.'),
            ExamResource(title='SAT Digital SAT Full Practice', category=sat, source_name='College Board',
                url='https://satsuite.collegeboard.org/digital/digital-practice-preparation', subject='General', difficulty='MEDIUM',
                exam_type='FULL_TEST', description='Official Digital SAT practice using Bluebook app from College Board. Adaptive format with two modules per section.'),
            ExamResource(title='GRE Math Flashcards', category=gre, source_name='Kaplan',
                url='https://www.kaptest.com/gre/free/gre-practice-test-options', subject='Math', difficulty='MEDIUM',
                exam_type='MINI_QUIZ', description='Essential GRE Math formulas and concepts flashcards from Kaplan for quick review.'),
            ExamResource(title='IELTS Cambridge Practice Tests 1-18', category=ielts, source_name='Cambridge University Press',
                url='https://www.cambridge.org/gb/cambridgeenglish/catalog/cambridge-english-exams-ielts/cambridge-ielts-1-18-academic', subject='General', difficulty='HARD',
                exam_type='FULL_TEST', description='The gold-standard Cambridge IELTS books with authentic past papers from Cambridge ESOL.'),
            ExamResource(title='TOEFL Grammar Practice', category=toefl, source_name='Grammarly',
                url='https://www.grammarly.com/blog/toefl/', subject='Grammar', difficulty='EASY',
                exam_type='MINI_QUIZ', description='Grammar review for TOEFL test takers focusing on common grammatical structures tested in the exam.'),
            ExamResource(title='GMAT Reading Comprehension Practice', category=gmat, source_name='Magoosh',
                url='https://gmat.magoosh.com/', subject='Verbal', difficulty='MEDIUM',
                exam_type='SECTION', description='GMAT Reading Comprehension passages with detailed strategy guides and explanations.'),
            ExamResource(title='AYT Fizik Soruları', category=ayt, source_name='ÖSYM',
                url='https://www.osym.gov.tr', subject='Fizik', difficulty='HARD',
                exam_type='SECTION', description='AYT Fizik bölümü için kapsamlı soru bankası. Mekanik, elektrik ve modern fizik konularını içerir.'),
            ExamResource(title='DGS Tam Deneme Sınavı', category=dgs, source_name='ÖSYM',
                url='https://www.osym.gov.tr', subject='Genel', difficulty='MEDIUM',
                exam_type='FULL_TEST', description='DGS için tam uzunlukta deneme sınavı. Sayısal ve sözel bölümlerin tamamını kapsar.'),
            ExamResource(title='ALES Kelime Bilgisi Mini Test', category=ales, source_name='ÖSYM',
                url='https://www.osym.gov.tr', subject='Sözel', difficulty='EASY',
                exam_type='MINI_QUIZ', description='ALES için kelime anlamı ve dil bilgisi mini testleri.'),
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
