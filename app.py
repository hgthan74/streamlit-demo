import streamlit as st

st.title("Chatbot tư vấn học môn Lịch sử")

question = st.text_input("Nhập câu hỏi:")

if question:

    question = question.lower()

    if "học lịch sử thế nào" in question:
        answer = """
        Để học tốt Lịch sử:
        - Đọc trước bài học.
        - Ghi nhớ các mốc thời gian quan trọng.
        - Vẽ sơ đồ tư duy.
        - Liên hệ các sự kiện với nhau.
        """

    elif "chiến thắng điện biên phủ" in question:
        answer = """
        Chiến thắng Điện Biên Phủ diễn ra năm 1954,
        kết thúc cuộc kháng chiến chống thực dân Pháp
        và dẫn tới Hiệp định Genève.
        """

    elif "cách nhớ sự kiện lịch sử" in question:
        answer = """
        Nên nhóm các sự kiện theo giai đoạn,
        lập bảng thời gian và thường xuyên ôn tập.
        """

    elif "ai là chủ tịch đầu tiên của việt nam" in question:
        answer = """
        Chủ tịch đầu tiên của nước Việt Nam Dân chủ Cộng hòa
        là Chủ tịch Hồ Chí Minh.
        """

    else:
        answer = """
        Xin lỗi, tôi chưa có câu trả lời cho câu hỏi này.
        """

    st.success(answer)