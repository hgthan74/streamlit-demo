import streamlit as st

st.title("Ứng dụng đầu tiên")

name = st.text_input("Nhập tên")

if name:
    st.success(f"Xin chào {name}")