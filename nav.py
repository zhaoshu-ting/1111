import streamlit as st

def show():
    st.markdown("""
    <style>
    .nav-bg {
        background-color: #1f4e79;
        padding:10px 20px;
        border-radius:4px;
    }
    .nav-btn > button{
        background:transparent;
        color:white;
        border:none;
        font-weight:700;
        font-size:16px;
        padding:8px 18px;
    }
    </style>
    """,unsafe_allow_html=True)
    st.markdown('<div class="nav-bg">',unsafe_allow_html=True)
    c1,c2,c3,c4 = st.columns([0.12,0.16,0.18,0.54])
    with c1:
        if st.button("首页",key="nav_home"):
            st.session_state.page="首页"
            st.rerun()
    with c2:
        if st.button("线上编码工具",key="nav_code"):
            st.session_state.page="线上编码工具"
            st.rerun()
    with c3:
        if st.button("利润投产测算",key="nav_profit"):
            st.session_state.page="利润投产测算"
            st.rerun()
    with c4:
        st.markdown("<div style='text-align:right'>",unsafe_allow_html=True)
        if st.button("退出登录",key="nav_logout"):
            st.session_state.login_ok=False
            st.session_state.page="首页"
            st.rerun()
        st.markdown("</div>",unsafe_allow_html=True)
    st.markdown("</div>",unsafe_allow_html=True)
