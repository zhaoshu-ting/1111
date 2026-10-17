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

# ========== 初始化session 必须放在最前面 ==========
if "login_ok" not in st.session_state:
    st.session_state.login_ok = False
if "page" not in st.session_state:
    st.session_state.page = "首页"

# 登录页面
if not st.session_state.login_ok:
    login.show()

else:
    # ========== 顶部导航（直接写在app里面，不再单独nav.py） ==========
    menu = ["首页", "线上编码工具", "利润投产测算"]
    # 横向单选框，key固定
    nav_choice = st.radio(
        label="导航菜单",
        options=menu,
        index=menu.index(st.session_state.page),
        horizontal=True,
        key="global_nav"
    )
    # 当radio选中值不等于session，更新并刷新
    if nav_choice != st.session_state.page:
        st.session_state.page = nav_choice
        st.rerun()

    # 退出登录按钮
    if st.button("退出登录"):
        st.session_state.login_ok = False
        st.session_state.page = "首页"
        st.rerun()

    # ========== 页面路由 ==========
    if st.session_state.page == "首页":
        home.show()
    elif st.session_state.page == "线上编码工具":
        page1.show()
    elif st.session_state.page == "利润投产测算":
        page2.show()
    else:
        home.show()
