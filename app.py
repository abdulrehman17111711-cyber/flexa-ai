import streamlit as st
from google import genai
from google.genai import types

st.title(" Flexa AI ")
st.write("Hello! How can I help you?")

# GitHub par code mein koi key nahi likhni! 
# Streamlit Cloud khud "st.secrets" se aap ki key utha legi.
if "gemini_key" in st.secrets:
    api_key = st.secrets["gemini_key"]
else:
    st.error("Streamlit Dashboard mein 'gemini_key' set nahi ki gayi!")
    st.stop()

try:
    client = genai.Client(api_key=api_key)

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Type question here..."):
        with st.chat_message("user"):
            st.markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.chat_message("assistant"):
            # Nayi library ka bilkul durust config format
            config = types.GenerateContentConfig(
                system_instruction="Aap ka naam Flexa hai. Aap aik AI assistant hain jise Abdul Rehman ne develop kiya hai. Jab bhi koi poochay ke aap ko kis ne banaya ya develop kiya, to hamesha proud hokar Abdul Rehman ka naam batayein."
            )
            
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt,
                config=config
            )
            st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
        
except Exception as e:
    st.error(f"API Error: {str(e)}")
        
