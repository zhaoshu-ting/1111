import streamlit as st
import login
import home
import page1
import page2

st.set_page_config(page_title="发财工具箱", layout="wide")

# 隐藏侧边栏
st.markdown("""
<style>
section[data-testid="stSidebar"]{
    display:none;
}
</style>
""",unsafe_allow_html=True)

# ========== 初始化session ==========
if "login_ok" not in st.session_state:
    st.session_state.login_ok = False
if "page" not in st.session_state:
    st.session_state.page = "首页"

# 登录界面
if not st.session_state.login_ok:
    login.show()

else:
    menu = ["首页", "线上编码工具", "利润投产测算"]
    # 重点：用value，删掉index！解决点击被重置的bug
    nav_choice = st.radio(
        "导航菜单",
        options=menu,
        value=st.session_state.page,
        horizontal=True,
        key="global_nav"
    )

    if nav_choice != st.session_state.page:
        st.session_state.page = nav_choice
        st.rerun()

    # 退出登录按钮
    if st.button("退出登录"):
        st.session_state.login_ok = False
        st.session_state.page = "首页"
        st.rerun()

    # 路由渲染页面
    if st.session_state.page == "首页":
        home.show()
    elif st.session_state.page == "线上编码工具":
        page1.show()
    elif st.session_state.page == "利润投产测算":
        page2.show()
    else:
        home.show()

import streamlit as st

st.set_page_config(layout="wide")

# 初始化
if "page" not in st.session_state:
    st.session_state.page = "首页"

menu = ["首页", "线上编码工具", "利润投产测算"]

# 【关键】不要用index！改用value绑定，去掉index，解决互相覆盖的bug
nav_choice = st.radio(
    "导航",
    options=menu,
    value=st.session_state.page,
    horizontal=True,
    key="global_nav"
)

# 选中值变更时更新session
if nav_choice != st.session_state.page:
    st.session_state.page = nav_choice
    st.rerun()

st.subheader(f"当前页面：{st.session_state.page}")
