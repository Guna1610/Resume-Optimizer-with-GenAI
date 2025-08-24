\# 📝 Resume Optimizer with GenAI



An AI-powered system to automatically tailor resumes to job descriptions for higher ATS (Applicant Tracking System) match rates.  

Built with \*\*Python, Google Gemini API, python-docx, and Streamlit\*\*.



---



\## 🚀 Features

\- \*\*Resume Parsing\*\*: Reads `.docx` resumes and extracts structured sections (Summary, Skills, Project Experience).

\- \*\*Job Description Handling\*\*: Loads `.txt`/pasted JDs and extracts relevant keywords.

\- \*\*GenAI Integration\*\*: Uses Google Gemini 1.5 Flash for LLM-driven rewriting of:

&nbsp; - \*\*Skills\*\* (categorized, ATS keyword alignment)

&nbsp; - \*\*Project Experience\*\* (action verbs, measurable outcomes, JD relevance)

\- \*\*Project Library\*\*: Automatically selects the \*\*top 3 projects\*\* most relevant to the JD from a full library.

\- \*\*Formatting Preservation\*\*: Maintains original Word resume layout (Times New Roman, indentation, bullet points, spacing).

\- \*\*Streamlit Web App\*\*:

&nbsp; - Left: Resume preview + inline editing of Summary, Skills, and Projects

&nbsp; - Right: JD Terminal (dark-mode input) + project library uploader

&nbsp; - One-click optimization → Download optimized `.docx`

\- \*\*Keyword Overlap Scoring\*\*: Rough ATS alignment score (percentage of JD keywords already in resume).



---



\## 📂 Project Structure

resume-optimizer-genai/

├── app.py # Streamlit UI

├── resume\_optimizer.py # Core pipeline

├── requirements.txt # Dependencies

├── projects.txt # Sample project library

├── sample\_resume.docx # Example resume

├── sample\_job.txt # Example job description

└── README.md # Documentation



\## ⚙️ Installation \& Setup



1\. Clone this repo:

&nbsp;  ```bash

&nbsp;  git clone https://github.com/<your-username>/resume-optimizer-genai.git

&nbsp;  cd resume-optimizer-genai



2\. Create virtual environment \& install deps:



&nbsp;  python -m venv venv

&nbsp;  source venv/bin/activate  # or venv\\Scripts\\activate on Windows

&nbsp;  pip install -r requirements.txt





3\. Create .env and add your Gemini API key:



&nbsp;  GOOGLE\_API\_KEY=your\_api\_key\_here





4\. Run the Streamlit app:



&nbsp;  streamlit run app.py





\## Usage



Upload your resume (.docx)



Paste or upload a JD (.txt)



Upload your full projects.txt (library of all projects)



Review/edit extracted sections in the left pane



Click Optimize Resume



Download ATS-optimized .docx



\## Tech Stack



Python



Google Gemini API (Generative AI)



Streamlit – interactive UI



python-docx – Word doc parsing/writing



dotenv – safe API key handling

