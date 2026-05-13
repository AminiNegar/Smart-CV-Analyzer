# 🤖 AI-Powered CV Analyzer

An intelligent resume parsing and job matching tool built with **Python**, **Streamlit**, and the **Llama 3.1** model via **Groq Cloud API**. This tool extracts key information from PDF resumes and evaluates how well they match a specific job description.

## 🎯 Features

- **PDF Text Extraction**: Seamlessly extracts raw text from PDF files using `PyMuPDF`.
- **AI Skill Extraction**: Automatically identifies technical and soft skills from the resume.
- **Smart Summarization**: Generates a professional overview of the candidate.
- **Job Matching Score**: Calculates a percentage match (0-100%) against a provided Job Description.
- **Gap Analysis**: Highlights missing skills to help candidates improve their resumes.
- **Modern UI**: Clean and responsive web interface with custom CSS tags.

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **AI Engine**: Groq Cloud API (Llama 3.1 8B Instant)
- **PDF Processing**: PyMuPDF (fitz)
- **Environment Management**: python-dotenv

## 🚀 Getting Started

### 1. Prerequisites
- Python 3.8+
- A Groq API Key

### 2. Installation
```bash
git clone [https://github.com/AminiNegar/cv-analyzer.git](https://github.com/AminiNegar/cv-analyzer.git)
cd cv-analyzer
pip install -r requirements.txt
```
### 3. Configuration
Create a .env file in the root directory:
```bash
GROQ_API_KEY=your_api_key_here
```
### 4. Running the App
```bash streamlit run main.py ```
🛡️ Security Note
This project uses .env files to protect sensitive API keys. A .gitignore file is included to prevent accidental uploads of credentials.

🥉 Project Credits
Developed as an AI-driven automation project focusing on unstructured data processing and prompt engineering.
