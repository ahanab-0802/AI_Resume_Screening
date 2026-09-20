# AI Resume Screener & Job Matcher

An AI-powered Resume Screening and Job Matching system developed for the **Cognizant NPN AIA Hackathon**.

The application analyzes a candidate's resume against a Job Description (JD), calculates an explainable match score, identifies matched and missing skills, measures semantic similarity, and provides actionable recommendations.

## 🚀 Project Overview

The system combines resume parsing, Job Description skill extraction, explicit skill matching, evidence-based validation, semantic similarity, explainable scoring, recommendations, authentication, analysis history, and PDF reporting.

The current MVP focuses on **one-to-one Resume ↔ Job Description matching**.

```text
Resume + Job Description
          ↓
     AI Analysis
          ↓
    JD Match Score
          ↓
 ┌────────┴────────┐
 ↓                 ↓
Matched Skills   Missing Skills
          ↓
    Recommendations
          ↓
      PDF Report
```

## 🎯 Problem Statement

Build an AI-powered Resume Screener & Job Matcher that can understand the relationship between a candidate's resume and a job description and provide a transparent explanation of the result.

Instead of returning only a numerical score, the system explains:
- Which JD skills are supported by the resume
- Which JD skills are missing or not sufficiently demonstrated
- How the JD match score is calculated
- How semantically similar the resume and JD are
- What can be improved in the resume

## 💡 Key Features

### 1. Resume Upload

Users can upload a resume for analysis.

The system extracts relevant information such as:
- Candidate name
- Skills
- Education
- Projects
- Experience
- Resume content

### 2. Job Description Analysis

The system extracts relevant requirements from the Job Description.

The parser focuses on actual skills such as programming languages, frameworks, libraries, tools, technical concepts, and professional/soft skills when explicitly required.

Normal responsibilities such as `Develop`, `Maintain`, `Collaborate`, and `Design` are not automatically treated as skills.

### 3. Evidence-Based Skill Matching

JD skills are checked against evidence from:

```text
Resume Skills
      ↓
Projects
      ↓
Experience
      ↓
Relevant Coursework
```

This allows legitimate evidence outside the main skills section to be considered.

## 🧠 AI / ML Components

### Semantic Similarity

The project uses the Sentence Transformer model:

```text
all-MiniLM-L6-v2
```

to calculate semantic similarity between the resume and Job Description.

### Explainable JD Match Score

The JD match score combines:

```text
80% → Explicit Skill Coverage
20% → Semantic Similarity
```

Formula:

```text
JD Match Score =
(0.80 × Skill Coverage)
+
(0.20 × Semantic Similarity)
```

where:

```text
Skill Coverage =
Matched JD Skills / Total JD Skills
```

This makes the score transparent and explainable.

## 🔍 Conservative Matching

The matching engine uses controlled aliases and explicit matching rules.

Examples:

```text
OOP
→ Object-Oriented Programming

DSA
→ Data Structures and Algorithms

ML
→ Machine Learning

DL
→ Deep Learning

CV
→ Computer Vision

sklearn
→ Scikit-learn
```

The system does not automatically assume that related technologies are equivalent.

For example:

```text
Machine Learning ≠ TensorFlow
Deep Learning ≠ TensorFlow
Google Colab ≠ Jupyter Notebook
Matplotlib ≠ Data Visualization
```

This helps reduce false-positive matches.

## 💡 Recommendations

After matching the resume with the JD, the system generates actionable recommendations based on the analysis.

Examples:

```text
Python found in resume
→ Make Python clearly visible in Skills/Projects.

Docker missing
→ Gain/use Docker and add genuine experience.

AWS mentioned in project
→ Explain which AWS service was used.

ML project has no metrics
→ Add model and evaluation metric if available.

JD requires REST API and relevant API experience exists
→ Explicitly mention REST API.

JD requires C++ but no evidence exists
→ Do not add C++ unless genuinely experienced.
```

The recommendation layer uses existing matching results instead of independently inventing missing qualifications.

## 📊 Dashboard

The application presents:
- ATS Resume Score
- JD Match Percentage
- Semantic Similarity
- Matched Skills
- Missing / Not Demonstrated Skills
- Explanation of the analysis
- Recommendations

## 📄 PDF Report

The application generates a clean PDF report containing:
- Candidate name
- ATS Resume Score
- JD Match Percentage
- Semantic Similarity
- Matched Skills
- Missing / Not Demonstrated Skills
- What This Means
- Recommendations

PDF generation is handled using **WeasyPrint**.

## 🗄️ Database & Authentication

The project uses **Supabase** for:
- Authentication
- Persistent analysis history
- Storing previous resume/JD analyses

The main analysis data is stored in the `analyses` table.

```text
User
 ↓
Authentication
 ↓
Resume + JD Analysis
 ↓
FastAPI Backend
 ↓
Supabase
 ↓
Analysis History
```

## 🏗️ System Architecture

```text
                    ┌──────────────────────┐
                    │        User          │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Streamlit Frontend   │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   FastAPI Backend    │
                    └──────────┬───────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
              ▼                ▼                ▼
       Resume Parser      JD Parser       Authentication
              │                │                │
              └────────────┬───┴────────────────┘
                           │
                           ▼
                 ┌─────────────────────┐
                 │   JD Skill Matcher  │
                 └──────────┬──────────┘
                            │
             ┌──────────────┼──────────────┐
             │              │              │
             ▼              ▼              ▼
      Explicit Skill   Evidence Check   Semantic
         Matching                       Similarity
             │              │              │
             └──────────────┼──────────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ Explainable Score   │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ Recommendations     │
                 └──────────┬──────────┘
                            │
              ┌─────────────┴─────────────┐
              ▼                           ▼
      Streamlit Dashboard           PDF Report
              │
              ▼
          Supabase
       Analysis History
```

## 🧩 Technology Stack

### Frontend
```text
Streamlit
HTML / CSS
```

### Backend
```text
Python
FastAPI
Uvicorn
```

### AI / NLP
```text
spaCy
Sentence Transformers
all-MiniLM-L6-v2
Groq
```

### Machine Learning
```text
Scikit-learn
NumPy
Pandas
```

### Database & Authentication
```text
Supabase
PostgreSQL
```

### PDF Generation
```text
WeasyPrint
```

### Development
```text
VS Code
GitHub
```

## 📁 Project Structure

```text
AI-Resume-Screener-Job-Matcher/
│
├── backend/
│   ├── api/
│   │   ├── auth.py
│   │   └── routes.py
│   ├── database/
│   │   └── supabase_db.py
│   ├── models/
│   │   └── schemas.py
│   ├── services/
│   │   ├── ats_scorer.py
│   │   ├── feedback_engine.py
│   │   ├── groq_parser.py
│   │   ├── jd_matcher.py
│   │   ├── pdf_export.py
│   │   ├── recommendation_engine.py
│   │   ├── report_generator.py
│   │   └── resume_parser.py
│   ├── templates/
│   │   └── summary.html
│   ├── core/
│   │   └── config.py
│   └── main.py
│
├── frontend/
│   └── streamlit_app.py
│
├── supabase/
│   └── schema.sql
│
├── requirements.txt
├── .gitignore
└── README.md
```

## 🔄 End-to-End Workflow

### Step 1 — Resume Upload

```text
Resume PDF
    ↓
Resume Parser
    ↓
Structured Resume Data
```

### Step 2 — Job Description

```text
Job Description
    ↓
JD Parser
    ↓
Required Skills
```

### Step 3 — Skill Matching

```text
Resume Data + JD Skills
          ↓
Explicit Skill Matching
```

### Step 4 — Evidence Verification

The matcher checks evidence from skills, projects, experience, and coursework.

### Step 5 — Semantic Similarity

```text
Resume Text
     +
JD Text
     ↓
Sentence Transformer
     ↓
Semantic Similarity
```

### Step 6 — Explainable Score

```text
80% Skill Coverage
+
20% Semantic Similarity
=
JD Match Score
```

### Step 7 — Explainability

The result contains matched skills, missing skills, skill coverage, semantic similarity, and score explanation.

### Step 8 — Recommendations

The system generates actionable recommendations from the analysis.

### Step 9 — Storage

The analysis can be stored in Supabase and viewed through history.

### Step 10 — PDF

The analysis can be exported as a PDF report.

## 🧪 Validation & Testing

The matching logic was manually tested with multiple resume-JD combinations.

Examples include:

### AI/ML Resume → Software Engineer JD

The system identified directly supported skills such as:

```text
Java
Python
DSA
OOP
SQL
```

and identified unsupported requirements as missing/not demonstrated.

### AI/ML Resume → Data Scientist JD

The system identified directly supported skills such as:

```text
Python
SQL
Pandas
NumPy
Scikit-learn
Machine Learning
Deep Learning
```

while avoiding unsupported assumptions such as:

```text
Matplotlib → Data Visualization
Google Colab → Jupyter Notebook
Machine Learning → TensorFlow
```

### Java/Spring Boot Resume → Data Scientist JD

The system produced limited overlap rather than treating unrelated technologies as matches.

### Java/Spring Boot Resume → Cybersecurity JD

The system identified only directly supported requirements and left unsupported cybersecurity skills as missing/not demonstrated.

## 🛡️ Design Principles

### Explainability
The system provides reasons behind the JD match result.

### Conservative Matching
A skill is not automatically considered matched simply because a related technology appears in the resume.

### Evidence-Based Analysis
Evidence can come from skills, projects, experience, and coursework.

### No Skill Fabrication
Recommendations should not encourage candidates to claim skills they do not genuinely possess.

### Modular Architecture
The project separates:

```text
Parsing
Matching
Scoring
Recommendations
Storage
Presentation
```

## 🔐 Security

Sensitive credentials should be stored using environment variables.

Example `.env`:

```text
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
GROQ_API_KEY=your_groq_api_key
```

Never commit `.env` or API keys to GitHub.

Recommended `.gitignore`:

```text
.env
__pycache__/
*.pyc
.venv/
venv/
```

## ⚙️ Local Setup

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd AI-Resume-Screener-Job-Matcher
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Windows:

```bash
venv\Scriptsctivate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create `.env`:

```text
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
GROQ_API_KEY=your_groq_api_key
```

### 5. Start the FastAPI backend

```bash
python -m uvicorn backend.main:app --reload
```

API documentation:

```text
http://127.0.0.1:8000/docs
```

### 6. Start the Streamlit frontend

Open another terminal:

```bash
python -m streamlit run frontend/streamlit_app.py
```

## 🔌 API Layer

FastAPI provides the backend API for:
- Authentication
- Resume analysis
- Job Description comparison
- Analysis results
- History
- PDF generation

Interactive API documentation is available through `/docs`.

## 📌 Current MVP Scope

```text
✓ Resume upload
✓ Job Description input
✓ Resume parsing
✓ JD skill extraction
✓ One-to-one Resume-JD matching
✓ Explicit skill matching
✓ Evidence-based skill validation
✓ Semantic similarity
✓ Explainable JD match score
✓ Matched skills
✓ Missing/not demonstrated skills
✓ Recommendations
✓ Authentication
✓ Analysis history
✓ PDF report generation
```

## 🚀 Future Enhancements

Possible future extensions include:
- Bulk resume screening
- Candidate ranking
- Recruiter dashboard
- Multiple JD comparison
- Interview question generation
- Multilingual resume support
- Bias/fairness analysis
- Advanced skill ontology
- More detailed experience matching
- Industry-specific matching models

These are future extensions and are not part of the current one-to-one MVP.

## 🏆 Hackathon Value

Instead of returning only:

```text
Match Score: 72%
```

the system provides:

```text
Match Score
     +
Matched Skills
     +
Missing Skills
     +
Evidence
     +
Semantic Similarity
     +
Recommendations
```

This makes resume-JD matching more transparent, explainable, and actionable.

## 👥 Team

Developed by a **6-member team** for the **Cognizant NPN AIA Hackathon**.

Team responsibilities span:
- AI/ML and NLP
- Resume and JD processing
- Backend/API development
- Database and authentication
- Frontend/dashboard
- Testing, documentation, and presentation

## 📜 Disclaimer

This system is an AI-assisted resume analysis tool.

The generated match score and recommendations are intended to support resume analysis and improvement. They should not be treated as a definitive hiring decision.

The system bases its analysis on the information available in the submitted resume and Job Description.

---

## ⭐ Project Summary

**AI Resume Screener & Job Matcher** combines explicit skill matching, evidence validation, and semantic similarity to analyze how closely a candidate's resume aligns with a Job Description.

The goal is to make Resume-JD matching:

```text
More Transparent
       +
More Explainable
       +
More Evidence-Based
       +
More Actionable
```

rather than relying only on simple keyword matching.
