### Resume Optimizer with GenAI

🚀 Resume Optimizer with GenAI is an AI-powered tool that tailors your resume to a given job description using Google Gemini API and python-docx.
It rewrites the Skills and Project Experience sections with ATS-friendly keywords, measurable outcomes, and professional phrasing while preserving the original formatting.

### ✨ Features
   -📂 Resume Parsing – Extracts structured text from .docx resumes.
   -📄 Job Description Parsing – Reads job descriptions from .txt.
   -🤖 AI-Powered Optimization –
        Skills section: grouped into bold categories (Programming, Visualization, ML, etc.).
        Project Experience: rewritten with action verbs, measurable results, and ATS keywords.
        Selects Top 3 most relevant projects from a user-provided project library.
   -🎨 Formatting Preservation – Keeps .docx layout, Times New Roman (12pt), indentation, and bullet style intact.
   -🔑 ATS Optimization – Seamlessly integrates keywords like Python, SQL, Tableau, Azure, MLOps, ETL.
   -📝 Output – Generates an ATS-friendly, recruiter-ready .docx resume.

### 🛠️ Tech Stack

-Python 3.10+
-Google Gemini API
 (google-generativeai)
-python-docx
   resume parsing & writing
-python-dotenv – manage API keys
(Future: ChromaDB + sentence-transformers for RAG-based project matching)

### 📂 Project Structure
ResumeOptimizer-GenAI/
│── resume_optimizer.py      # Main script – parse, optimize, and rewrite resume sections
│── projects.txt             # Project library (all your projects listed here)
│── sample_resume.docx       # Input resume example
│── sample_job.txt           # Job description example
│── optimized_resume.docx    # Output ATS-optimized resume
│── requirements.txt         # Dependencies
│── README.md                # Documentation


### How It Works

Place your resume in .docx format (sample_resume.docx).
Add the job description in .txt (sample_job.txt).
Add your full project library in projects.txt.
Run the script:
python resume_optimizer.py
Get your ATS-optimized resume in optimized_resume.docx 🎉

### 📦 Installation

Clone the repository:
       git clone https://github.com/<your-username>/Resume-Optimizer-with-GenAI.git
       cd Resume-Optimizer-with-GenAI

Create a virtual environment and install dependencies:
        python -m venv venv
        source venv/bin/activate   # (Linux/Mac)
        venv\Scripts\activate      # (Windows)

        pip install -r requirements.txt

Set up your Google Gemini API key:
        Get a free key from Google AI Studio
.       Create a .env file in the project root:
                                       GOOGLE_API_KEY=your_api_key_here

### Future Enhancements

 Add Streamlit/Gradio UI for drag-and-drop resume optimization.
 Support PDF parsing for resumes & job descriptions.
 Integrate ChromaDB for semantic project matching.
 Export in LaTeX/Markdown resume templates.

 ### 📜 License

This project is licensed under the MIT License – free to use and modify.
