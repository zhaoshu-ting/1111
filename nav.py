import streamlit as st

def show():
    menu_list = ["首页", "线上编码工具", "利润投产测算"]
    current = st.session_state.page
    selected_page = st.selectbox("页面导航", menu_list, index=menu_list.index(current))

    if selected_page != current:
        st.session_state.page = selected_page
        st.rerun()

    if st.button("退出登录"):
        st.session_state.login_ok = False
        st.session_state.page = "首页"
        st.rerun()
