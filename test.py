import streamlit as st
import random

st.set_page_config(page_title="Dỗ người yêu", page_icon="💖", layout="centered")

st.markdown("""
    <h1 style='text-align:center; color:#ff4b6e;'>Em đừng giận anh nữa nha 💖</h1>
""", unsafe_allow_html=True)

# CSS để nút “Không” bay lung tung
st.markdown("""
    <style>
    div.stButton > button:first-child {
        transition: all 0.25s ease;
    }
    </style>
""", unsafe_allow_html=True)

# Khu chia cột (giả lập to hơn để có không gian chạy)
col1, col2, col3, col4, col5 = st.columns(5)

if "no_pos" not in st.session_state:
    st.session_state.no_pos = random.choice(["col1", "col2", "col3", "col4", "col5"])

# Nút “Vâng”
with col3:
    yes = st.button("💞 Vâng", key="yes")

# Nút “Không” di chuyển ngẫu nhiên
no_col = {
    "col1": col1, "col2": col2, "col3": col3, "col4": col4, "col5": col5
}[st.session_state.no_pos]
with no_col:
    no = st.button(" Không", key="no")

# Nếu bấm “Vâng”
if yes:
    st.success("Anh yêu em nhìu lắm ạaaaa 💕")

# Nếu bấm “Không” → chạy ngay
if no:
    st.session_state.no_pos = random.choice(["col1", "col2", "col3", "col4", "col5"])
    st.rerun()

# 🌀 Tự động làm “Không” chạy khi di chuột gần (fake bằng cách random mỗi lần refresh)
import time
if random.random() < 0.25:  # 25% cơ hội đổi vị trí mỗi lần trang reload
    st.session_state.no_pos = random.choice(["col1", "col2", "col3", "col4", "col5"])
    time.sleep(0.1)
    st.rerun()
