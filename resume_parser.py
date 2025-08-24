import docx


# Function to extract text from .docx resume
def extract_resume_text(file_path):
    doc = docx.Document(file_path)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return "\n".join(full_text)


# Function to extract text from .txt job description
def extract_job_text(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


# Test run
if __name__ == "__main__":
    resume_text = extract_resume_text("sample_resume.docx")  # put your resume file here
    job_text = extract_job_text("sample_job.txt")  # put your job description here

    print("===== RESUME TEXT =====")
    print(resume_text[:500])  # print first 500 chars

    print("\n===== JOB DESCRIPTION TEXT =====")
    print(job_text[:500])  # print first 500 chars
