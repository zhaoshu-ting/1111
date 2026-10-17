import streamlit as st

def show():
    menu_list = [
        ("首页", "首页"),
        ("线上编码工具", "线上编码工具"),
        ("利润投产测算", "利润投产测算")
    ]
    cols = st.columns(len(menu_list))
    for idx, (label, page_name) in enumerate(menu_list):
        with cols[idx]:
            # 当前页面高亮
            if st.button(label, type="primary" if st.session_state.page == page_name else "secondary"):
                st.session_state.page = page_name
                st.rerun() # 点击立刻刷新页面

    # 退出登录按钮
    if st.button("退出登录"):
        st.session_state.login_ok = False
        st.session_state.page = "首页"
        st.rerun()
