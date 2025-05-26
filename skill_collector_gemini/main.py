import os
from dotenv import load_dotenv
load_dotenv()
from extractor.pdf_reader import extract_text_from_pdf
from extractor.gemini_prompt import extract_resume_data_with_gemini

def main():
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    sample_resumes_folder_name = "Sample Resumes"
    pdf_filename = "sample_resume.pdf"

    resume_path = os.path.join(script_dir, sample_resumes_folder_name, pdf_filename)
    #resume_path = "sample_resume.pdf"  # Replace with your file path
    text = extract_text_from_pdf(resume_path)
    result = extract_resume_data_with_gemini(text)
    print(result)

if __name__ == "__main__":
    main()


