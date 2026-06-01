import streamlit as st

st.title("Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.write(msg)

prompt = st.text_input("Nhập câu hỏi")

if prompt:

    answer = f"Tôi nhận được: {prompt}"

    st.session_state.messages.append(
        f"Bạn: {prompt}"
    )

    st.session_state.messages.append(
        f"Bot: {answer}"
    )

    st.rerun()