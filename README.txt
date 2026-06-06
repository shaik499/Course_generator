# 🎓 AI Course Generator

An AI-powered course generation platform built with Python, Streamlit, and Groq LLMs. Generate complete professional course outlines, learning outcomes, weekly modules, quizzes, and assignments in seconds.

## 🚀 Features

* Generate complete course structures using AI
* Create learning outcomes automatically
* Generate weekly modules and lesson plans
* Create quizzes and assignment ideas
* Save generated courses locally
* Course library for viewing previous courses
* Export courses as PDF
* Export courses as DOCX
* Modern Streamlit-based interface
* Powered by Groq LLMs

---

## 🛠️ Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### AI

* Groq API
* Llama 3.3 70B

### Document Generation

* ReportLab (PDF)
* python-docx (DOCX)

### Storage

* JSON

---

## 📂 Project Structure

```text
AI_Course_Generator
│
├── app.py
├── course_generator.py
├── course_storage.py
├── export_utils.py
├── requirements.txt
├── .env
│
└── generated_courses
    ├── pdf
    ├── docx
    └── text
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/AI_Course_Generator.git
cd AI_Course_Generator
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=YOUR_GROQ_API_KEY
```

Get a free API key from Groq.

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

---

## 📖 Usage

1. Enter a course topic
2. Select level
3. Choose duration
4. Select audience
5. Click **Generate Course**
6. Download PDF or DOCX
7. Access saved courses from the Course Library

---

## 📄 Example Output

The AI generates:

* Course Title
* Course Description
* Learning Outcomes
* Weekly Modules
* Lesson Plans
* Quiz Questions
* Assignments

---

## 🔮 Future Improvements

* Course templates
* Course search
* Course deletion
* Presentation (PPTX) export
* Multi-language support
* Islamic course generation mode
* User authentication
* Cloud database integration

---

## 💡 Motivation

This project was developed to simplify curriculum creation for educators, trainers, institutions, and content creators by leveraging modern large language models.

---

## 👨‍💻 Author

Farooq Shaik

GitHub: https://github.com/farooq499
LinkedIn: https://www.linkedin.com/in/shaik-farooq-b01860242?utm_source=share_via&utm_content=profile&utm_medium=member_android

---

## 📜 License

This project is licensed under the MIT License.
