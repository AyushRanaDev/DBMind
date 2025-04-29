# DBMind

🧠 A mini AI-powered DBMS project using Streamlit + Google Gemini + SQLite.

## 🔧 Features:
- Ask English questions → Get SQL query answers
- Insert, Update, Delete, View student records
- Real-time updates via Streamlit interface
- Uses Google Gemini to generate SQL from natural language

## 📁 Files:
- `app.py`: Main application (UI + logic)
- `sql.py`: DB functions for CRUD
- `student.db`: SQLite DB (not uploaded for privacy)
- `.env`: 🔐 Holds your Google API key (DO NOT UPLOAD)
- `requirements.txt`: Needed Python packages

## 🛡️ Setup:
Create a `.env` file in this format:
```env
GOOGLE_API_KEY="your-own-gemini-api-key"
