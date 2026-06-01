import streamlit as st

st.title("Chatbot đầu tiên")

question = st.text_input("Nhập câu hỏi")

if question:
    st.write("Bot:", "Bạn vừa nhập: " + question)