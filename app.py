import streamlit as st
import os
from groq import Groq

# 1. Page Configuration (ChatGPT Dark Theme Look)
st.set_page_config(page_title="Flexa AI", page_icon="🤖", layout="centered")
st.markdown("""
    <style>
    .stApp { background-color: #131314; color: #e3e3e3; }
    </style>
""", unsafe_allow_html=True)

st.title("🤖 Flexa AI Chatbot")
st.caption("Powered by Groq & Streamlit | Pure Coding Control")

# 2. Key security setting (Hugging Face ke Secret se automatic uthayega)
api_key = os.environ.get("GROQ_API_KEY")
client = Groq(api_key=api_key)

# 3. Chat History Database (Session State Control)
if "messages" not in st.session_state:
    st.session_state.messages = []

# Purani chat logs screen par dikhana
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 4. User input aur AI backend call
if prompt := st.chat_input("How I can help you today..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        try:
            # Model Control (Aap yahan deepseek-r1 ya llama3 badal sakte hain)
            completion = client.chat.completions.create(
                model="llama-3.3-70b-versatile", 
                messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
            )
            full_response = completion.choices[0].message.content
            message_placeholder.markdown(full_response)
        except Exception as e:
            full_response = f"Jani backend connect ho gaya hai, bas Hugging Face ki Settings me 'GROQ_API_KEY' add karna baqi hai."
            message_placeholder.markdown(full_response)
            
    st.session_state.messages.append({"role": "assistant", "content": full_response})
  
