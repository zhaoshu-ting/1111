import streamlit as st

# 回调函数：修改页面
def change_page():
    st.session_state.page = st.session_state.nav_selector

def show():
    menu_list = ["首页", "线上编码工具", "利润投产测算"]
    # 下拉框，绑定key，指定on_change
    st.selectbox(
        "页面导航",
        options=menu_list,
        index=menu_list.index(st.session_state.page),
        key="nav_selector",
        on_change=change_page
    )

    if st.button("退出登录"):
        st.session_state.login_ok = False
        st.session_state.page = "首页"
        st.rerun()
