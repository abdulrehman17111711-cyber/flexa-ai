import streamlit as st
from google import genai

st.title(" Flexa AI ")
st.write("Welcome! How can I help you today?.")

# YAHAN APNI KEY PASTE KRAIN (Inverted commas ke andar)
ASLI_API_KEY = "AQ.Ab8RN6K5KaV1WczGydC_9coL3sYu-I8ndd_Txt0k-iwPsPLbLw"

try:
    client = genai.Client(api_key=ASLI_API_KEY)

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Ask flexa a question..."):
        with st.chat_message("user"):
            st.markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.chat_message("assistant"):
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt,
                config={
                    'system_instruction': 'Aap ka naam Alexa hai. Aap aik AI assistant hain jise Abdul Rehman ne develop kiya hai. Jab bhi koi poochay ke aap ko kis ne banaya ya develop kiya, to hamesha proud hokar Abdul Rehman ka naam batayein.'
                }
            )
            st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
        
except Exception as e:
    st.error("API Key mein koi masla hai. Meharbani kar ke check krain.")
    
