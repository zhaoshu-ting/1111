import streamlit as st

def show():
    menu_list = ["首页", "线上编码工具", "利润投产测算"]
    # radio 横向排布
    selected = st.radio(
        "页面导航",
        options=menu_list,
        index=menu_list.index(st.session_state.page),
        horizontal=True,
        key="main_nav_radio"
    )
    # 检测是否切换
    if selected != st.session_state.page:
        st.session_state.page = selected
        st.rerun()

    # 退出登录按钮
    if st.button("退出登录"):
        st.session_state.login_ok = False
        st.session_state.page = "首页"
        st.rerun()
