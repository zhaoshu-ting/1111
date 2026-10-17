import streamlit as st
import login
import home
import page1
import page2

st.set_page_config(page_title="发财", layout="wide")

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

# 导航切换回调函数
def change_page():
    st.session_state.page = st.session_state["global_nav"]

# 登录界面
if not st.session_state.login_ok:
    login.show()

else:
    menu = ["首页", "线上编码工具", "利润投产测算"]
    # 旧版本只能用index，on_change回调，key绑定
    st.radio(
        "导航菜单",
        options=menu,
        index=menu.index(st.session_state.page),
        horizontal=True,
        key="global_nav",
        on_change=change_page
    )

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
