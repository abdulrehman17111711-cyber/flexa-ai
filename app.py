import streamlit as st
from google import genai

# App ki screen pr upar naam badal diya hai
st.title("Flexa AI Chatbot")
st.write("Welcome! Main aap ki har tarah se madad krne k liye tayyar hoon.")

# Gemini Free API Key input box
api_key = st.text_input("AQ.Ab8RN6K5KaV1WczGydC_9coL3sYu-I8ndd_Txt0k-iwPsPLbLw", type="password")

if api_key:
    client = genai.Client(api_key=api_key)

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Alexa se kuch bhi poochein..."):
        with st.chat_message("user"):
            st.markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.chat_message("assistant"):
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt,
            )
            st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
else:
    st.warning("Meharbani kr k pehle apni Gemini API Key enter krain taake Alexa kaam kr skay.")
    
