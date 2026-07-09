import streamlit as st
from google import genai

st.title(" Flexa AI ")
st.write("Welcome! How can I help you ?")

# Key ko permanent save karne ke liye settings
if "saved_api_key" not in st.session_state:
    st.session_state.saved_api_key = "AQ.Ab8RN6K5KaV1WczGydC_9coL3sYu-I8ndd_Txt0k-iwPsPLbLw"

# --- API KEY SETTING ---
# Inverted commas "" ke andar apni QP... wali key paste kar dain
if "saved_api_key" not in st.session_state or not st.session_state.saved_api_key:
    st.session_state.saved_api_key = "YAHAN_APNI_QP_WALI_KEY_PASTE_KRAIN"
# -----------------------

# Jab key mil jaye to chatbot shuru karo
if st.session_state.saved_api_key:
    try:
        client = genai.Client(api_key=st.session_state.saved_api_key)

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
                # Alexa ke dimaag mein aap ka naam daal diya hai
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=prompt,
                    config={
                        'system_instruction': 'Aap ka naam Flexa hai. Aap aik AI assistant hain jise Abdul Rehman ne develop kiya hai. Jab bhi koi poochay ke aap ko kis ne banaya ya develop kiya, to hamesha proud hokar Abdul Rehman ka naam batayein.'
                    }
                )
                st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
            
    except Exception as e:
        st.error("API Key mein koi masla hai. Meharbani kar ke check krain.")
        if st.button("Key Dubara Enter Krain"):
            st.session_state.saved_api_key = ""
            st.rerun()
else:
    st.warning("Meharbani kr k pehle apni Gemini API Key enter krain taake Alexa kaam kr skay.")
    
