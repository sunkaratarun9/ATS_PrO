# ATS Resume Skill Collector (Powered by Gemini)

### 🔍 Description
This project extracts structured skill, domain, and role data from resumes using Gemini LLM.

### 🚀 How It Works
1. Extracts text from uploaded PDF resume
2. Sends resume text to Gemini API
3. Returns JSON with:
   - `tech_skills` (with count)
   - `strengths` (with count)
   - `domain` (with count)
   - `current_job`
   - `targeted_job`

### 🧪 Run Locally
```bash
pip install -r requirements.txt
python app.py
or
flask run