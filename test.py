import streamlit as st
import random
import time

# ⚙️ Cấu hình trang
st.set_page_config(page_title="Dỗ người yêu", page_icon="💖", layout="centered")

# 💅 CSS: nền xanh đậm + hiệu ứng nút
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0a192f, #1b263b);
        color: white;
        font-family: "Comic Sans MS", cursive;
    }
    h1 {
        color: #ff6fa3;
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        text-shadow: 1px 1px 2px #000;
        margin-bottom: 10px;
    }
    p {
        text-align: center;
        font-size: 20px;
        color: #e0e0e0;
        margin-top: -5px;
    }
    div[data-testid="stButton"] > button {
        border-radius: 15px;
        font-weight: bold;
        border: 2px solid #90caf9;
        box-shadow: 0 4px 10px rgba(255, 255, 255, 0.2);
        transition: all 0.3s ease;
    }
    div[data-testid="stButton"] > button:hover {
        background-color: #90caf9;
        color: white !important;
        transform: scale(1.05);
    }
    </style>
""", unsafe_allow_html=True)

# 💖 Tiêu đề
st.markdown("<h1>Em đừng giận anh nữa nha 💖</h1>", unsafe_allow_html=True)
# 📦 Chia cột (cho không gian nút chạy)
col1, col2, col3, col4, col5 = st.columns(5)

# 🧠 Khởi tạo trạng thái
if "no_pos" not in st.session_state:
    st.session_state.no_pos = random.choice(["col1", "col2", "col3", "col4", "col5"])

if "no_size" not in st.session_state:
    st.session_state.no_size = 20  # Kích thước chữ mặc định

# 💞 Nút “Vâng”
with col3:
    yes = st.button("💞 Vâng", key="yes")

# 🙅‍♀️ Nút “Không” — điều chỉnh kích thước theo lần bấm
style = f"""
    <style>
    div[data-testid="stButton"][key="no"] > button {{
        font-size: {st.session_state.no_size}px !important;
        padding: 6px 14px !important;
    }}
    </style>
"""
st.markdown(style, unsafe_allow_html=True)

no_col = {
    "col1": col1, "col2": col2, "col3": col3, "col4": col4, "col5": col5
}[st.session_state.no_pos]
with no_col:
    no = st.button(" Không", key="no")

# 💬 Hành động khi bấm nút
if yes:
    st.success("Anh yêu em nhiều lắm ạaaaa 💕💐")

if no:
    st.session_state.no_pos = random.choice(["col1", "col2", "col3", "col4", "col5"])
    st.session_state.no_size = max(10, st.session_state.no_size - 2)  # giảm dần kích thước
    st.rerun()

# 🔄 “Không” tự chạy ngẫu nhiên một chút (tăng vui)
if random.random() < 0.2:  # 20% xác suất đổi vị trí mỗi lần refresh
    st.session_state.no_pos = random.choice(["col1", "col2", "col3", "col4", "col5"])
    time.sleep(0.1)
    st.rerun()
