import streamlit as st

def show():
    current_page = st.session_state.get("page", "首页")
    c1,c2,c3,c4 = st.columns([1,1,1,2])
    with c1:
        if st.button("首页",key="nav_home"):
            st.session_state.page = "首页"
            st.rerun()
    with c2:
        if st.button("线上编码工具",key="nav_code"):
            st.session_state.page = "线上编码工具"
            st.rerun()
    with c3:
        if st.button("利润投产测算",key="nav_profit"):
            st.session_state.page="利润投产测算"
            st.rerun()
    with c4:
        if st.button("退出登录",key="nav_logout"):
            st.session_state.login_ok=False
            st.session_state.page="首页"
            st.rerun()
