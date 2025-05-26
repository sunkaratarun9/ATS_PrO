import os
import google.generativeai as genai

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def extract_resume_data_with_gemini(resume_text: str) -> str:
    model = genai.GenerativeModel("models/gemini-1.5-pro")

    prompt = f"""
You are a highly precise resume analyzer.

Your job is to read the resume text and return **only a valid JSON** in the format below — with no explanation, markdown, or quotes.

---

### Definitions:
- "tech_skills": Technical tools, programming languages, frameworks, cloud platforms, etc.
- "strengths": Personality and soft skills like Leadership, Problem-solving, Communication, Teamwork, Adaptability, etc.
  ⚠️ Do NOT include project achievements or task descriptions as strengths.
- "domain": Work areas or industries like NLP, DevOps, Healthcare, Marketing, Cloud, etc.
- "suggested_*": Suggest 3–5 highly relevant items missing from the resume with a short reason for each.

---

### Resume Content:
\"\"\"
{resume_text}
\"\"\"

---

### Required Output (strict JSON only):
{{
  "tech_skills": ["<list of technical skills>"],
  "tech_skills_count": <number>,
  "suggested_tech_skills": {{
    "<missing tech skill>": "why it's relevant",
    "<another>": "why"
  }},

  "strengths": ["<list of soft skills only>"],
  "strengths_count": <number>,
  "suggested_strengths": {{
    "<missing soft skill>": "why it's useful for the role"
  }},

  "domain": ["<list of work domains>"],
  "domain_count": <number>,
  "suggested_domain": {{
    "<missing domain>": "why it's relevant"
  }},

  "current_job": "<job title if found>",
  "targeted_job": "<target job if found or null>"
}}
"""

    response = model.generate_content(prompt)
    return response.text.strip()
