import streamlit as st
from groq import Groq
from datetime import datetime

# --- Page Title ---
st.title("🩺 Welcome to Doctor AI")


# --- Sidebar Configuration ---
with st.sidebar:
    st.image("A:/VScode/SAMPLEE.PNG")  # Adjust path if needed
    st.subheader("🔐 Configuration")
    
    api_key = st.text_input("Enter your API key", type="password")
    model_option = ["llama3-70b-8192", "llama-3.3-70b-versatile"]
    selected_models = st.selectbox("Select a model", model_option)

    # 🔒 Hidden system prompt (hardcoded)
    system_prompt = "Act As A Doctor"

    st.markdown("-------")
    st.markdown("### ℹ️ About")
    st.markdown("This chatbot is powered by **GROQ API**.")
    st.markdown("Designed to simulate a doctor for educational and informational purposes.")


# --- Session State Initialization ---
if "messages" not in st.session_state:
    st.session_state.messages = []

if "api_configured" not in st.session_state:
    st.session_state.api_configured = False


# --- GROQ Client Setup ---
if api_key:
    try:
        client = Groq(api_key=api_key)
        st.session_state.api_configured = True
    except Exception as e:
        st.error(f"Error configuring GROQ client: {e}")
        st.stop()


# --- Display Conversation History ---
for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.write(message['content'])


# --- User Input ---
prompt = st.chat_input("What can I help you with today?")

if prompt:
    if not st.session_state.api_configured:
        st.error("Please enter a valid GROQ API Key!")
    else:
        # Store user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)

        # Generate response from GROQ
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            try:
                with st.spinner("Thinking..."):
                    message_for_api = [{"role": "system", "content": system_prompt}]
                    message_for_api.extend([
                        {"role": m["role"], "content": m["content"]}
                        for m in st.session_state.messages
                    ])

                    chat_completion = client.chat.completions.create(
                        messages=message_for_api,
                        model=selected_models
                    )

                    reply = chat_completion.choices[0].message.content
                    message_placeholder.write(reply)

                    # Save assistant response
                    st.session_state.messages.append({"role": "assistant", "content": reply})

            except Exception as e:
                st.error(f"⚠️ No response. Error: {str(e)}")
