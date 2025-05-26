from flask import Flask, request, jsonify
from dotenv import load_dotenv
load_dotenv()
from extractor.pdf_reader import extract_text_from_pdf
from extractor.gemini_prompt import extract_resume_data_with_gemini
import os
import json
import tempfile
import re

app = Flask(__name__)


@app.route("/analyze_resume", methods=["POST"])
def analyze_resume():
    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files["file"]
    if not file.filename.endswith(".pdf"):
        return jsonify({"error": "Only PDF files are supported"}), 400

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
        file.save(temp_file.name)
        resume_text = extract_text_from_pdf(temp_file.name)
        gemini_response = extract_resume_data_with_gemini(resume_text)

    try:
        # ✅ Extract only the valid JSON content from Gemini's markdown-wrapped output
        cleaned = re.search(r'{.*}', gemini_response, re.DOTALL)
        if not cleaned:
            raise ValueError("Gemini output did not contain valid JSON")

        parsed_json = json.loads(cleaned.group(0))
        return jsonify(parsed_json), 200

    except Exception as e:
        return jsonify({
            "error": "Gemini did not return valid JSON",
            "raw": gemini_response,
            "message": str(e)
        }), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
