import streamlit as st

def change_page_pills():
    st.session_state.page = st.session_state.nav_pill

def show():
    menu_list = ["首页", "线上编码工具", "利润投产测算"]
    st.pills(
        "导航菜单",
        options=menu_list,
        selection_mode="single",
        default=st.session_state.page,
        key="nav_pill",
        on_change=change_page_pills
    )

    if st.button("退出登录"):
        st.session_state.login_ok = False
        st.session_state.page = "首页"
        st.rerun()
