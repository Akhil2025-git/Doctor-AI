# 🩺 Doctor AI - Streamlit Chatbot Using GROQ API

Doctor AI is a Streamlit web application that simulates a virtual doctor for educational and informational purposes. It uses the GROQ API with LLaMA models to generate responses based on user prompts in a conversational style.

## 🚀 Features

- Secure API key input through the sidebar.
- Selection of LLaMA-based GROQ models (`llama3-70b-8192`, `llama-3.3-70b-versatile`).
- Dynamic chat interface using `st.chat_input` and `st.chat_message`.
- Session-based conversation memory.
- Custom system prompt to guide AI behavior ("Act As A Doctor").
- Sidebar with branding and application description.

## 📦 Requirements

- Python 3.8+
- [Streamlit](https://streamlit.io/)
- GROQ api

Install dependencies:

```bash
pip install streamlit groq
```

## 🛠️ How to Run

1. Clone this repository or download the `.py` file.

2. Set up the image path correctly in the code if using a custom image:
   ```python
   st.image("A:/VScode/SAMPLEE.PNG")  # Change this path to your actual image location
   ```

3. Run the app:
   ```bash
   streamlit run your_file_name.py
   ```

4. Enter your GROQ API key in the sidebar to start chatting.

## 📁 File Structure

```
DoctorAI/
├── doctor_ai_app.py
├── SAMPLEE.PNG
└── README.md
```

## 💡 Notes

- This chatbot is **not** intended for real medical advice. It is a demonstration of conversational AI using a healthcare theme.
- You must have a valid GROQ API key to use the chatbot.

## 📜 License

This project is for educational use only.
