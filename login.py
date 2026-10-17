import streamlit as st

def show():
    st.markdown("""
    <style>
    .stApp {
        background: #e8f1fc;
    }
    .login-card {
        background: #ffffff;
        width: 480px;
        margin: 18vh auto 0 auto;
        padding: 36px 40px;
        border-radius: 18px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.12);
    }
    .login-title {
        text-align: center;
        font-size: 28px;
        font-weight: 800;
        color: #111111;
        margin-bottom: 8px;
    }
    .login-subtitle {
        text-align: center;
        font-size: 14px;
        color: #444444;
        margin-bottom: 24px;
    }
    .login-card label {
        color: #111111 !important;
        font-weight: 600;
    }
    .login-card input {
        color: #111111;
    }
    .login-card button {
        width: 100%;
        background-color: #1f4e79;
        color: #ffffff;
        font-weight: 700;
        border-radius: 10px;
        padding: 10px 0;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="login-card">', unsafe_allow_html=True)
    st.markdown('<div class="login-title">发财</div>', unsafe_allow_html=True)
    st.markdown('<div class="login-subtitle">商品资料与线上编码管理平台</div>', unsafe_allow_html=True)

    username = st.text_input("登录名称", key="login_name")
    password = st.text_input("登录密码", type="password", key="login_pwd")

    if st.button("登录"):
        if username == "admin" and password == "12345678":
            st.session_state.login_ok = True
            st.session_state.page = "首页"
            st.rerun()
        else:
            st.error("账号或密码错误")

    st.markdown('</div>', unsafe_allow_html=True)
