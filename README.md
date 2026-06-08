# ExamFind — AI-Powered Exam Resource Finder

A Django web application that helps students find free practice tests for standardized exams using AI-powered natural language search. Powered by Groq (free AI API).

## Features

- AI-powered natural language search (Groq llama-3.3-70b, free)
- 60+ curated free resources for SAT, ACT, IELTS, TOEFL, GRE, GMAT, Cambridge, YKS, TYT, AYT, KPSS, DGS, ALES
- User registration, login, forgot password
- Save tests, add personal notes, track completion
- Personal dashboard with search history
- Full admin panel for content management
- 100% free to run — no paid APIs, no paid hosting required

## Setup

1. Make sure Python 3.10+ is installed
2. `git clone` or download the project
3. `cd examfind`
4. `python -m venv venv`
5. Windows: `venv\Scripts\activate` | Mac/Linux: `source venv/bin/activate`
6. `pip install -r requirements.txt`
7. Copy `.env.example` to `.env`
8. Get a free Groq API key at https://console.groq.com (free, no credit card)
9. Add your Groq API key to `.env`
10. `python manage.py migrate`
11. `python manage.py seed_data`
12. `python manage.py runserver`
13. Open http://127.0.0.1:8000

## Default Credentials

- **Admin panel:** http://127.0.0.1:8000/admin → username: `admin`, password: `admin123`
- **Sample student:** username: `student1`, password: `pass123`

> **Note:** The app works without a Groq API key — it falls back to basic keyword search automatically.
