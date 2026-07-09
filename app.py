import streamlit as st
from google import genai

st.title(" Flexa AI ")
st.write("Welcome! How can I help you ?")

# Key ko permanent save karne ke liye settings
if "saved_api_key" not in st.session_state:
    st.session_state.saved_api_key = "AQ.Ab8RN6K5KaV1WczGydC_9coL3sYu-I8ndd_Txt0k-iwPsPLbLw"

# Agar pehle se key enter ki hui hai to query param se utha lo
if not st.session_state.saved_api_key and "key" in st.query_params:
    st.session_state.saved_api_key = st.query_params["key"]

# Agar key nahi hai to input box dikhao
if not st.session_state.saved_api_key:
    api_key_input = st.text_input("Apni Gemini API Key yahan enter krain:", type="password")
    if api_key_input:
        st.session_state.saved_api_key = api_key_input
        st.query_params["key"] = api_key_input
        st.rerun()

# Jab key mil jaye to chatbot shuru karo
if st.session_state.saved_api_key:
    try:
        client = genai.Client(api_key=st.session_state.saved_api_key)

        if "messages" not in st.session_state:
            st.session_state.messages = []

        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        if prompt := st.chat_input(" Ask flexa a question..."):
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
            
    except Exception as e:
        st.error("API Key mein koi masla hai. Meharbani kar ke check krain.")
        if st.button("Key Dubara Enter Krain"):
            st.session_state.saved_api_key = ""
            st.query_params.clear()
            st.rerun()
else:
    st.warning("Meharbani kr k pehle apni Gemini API Key enter krain taake Alexa kaam kr skay.")
    
