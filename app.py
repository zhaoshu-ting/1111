import streamlit as st
import login
import nav
import home
import page1
import page2

st.set_page_config(page_title="发财工具箱", layout="wide")

# ========== 全局样式：登录后纯白背景 ==========
st.markdown("""
<style>
div[data-testid="stAppViewContainer"] {
    background-color: #ffffff;
}
section[data-testid="stSidebar"] {
    display: none;
}
</style>
""", unsafe_allow_html=True)

# ========== 登录判断 ==========
if "login_ok" not in st.session_state:
    st.session_state.login_ok = False
if "page" not in st.session_state:
    st.session_state.page = "首页"

# URL参数控制
query_params = st.query_params
if "page" in query_params:
    p = query_params["page"]
    if p in ["首页", "线上编码工具", "利润投产测算"]:
        st.session_state.page = p
if "logout" in query_params:
    st.session_state.login_ok = False
    st.session_state.page = "首页"

# ========== 页面路由 ==========
if not st.session_state.login_ok:
    login.show()
else:
    nav.show()

    page = st.session_state.page

    if page == "首页":
        home.show()
    elif page == "线上编码工具":
        page1.run()
    elif page == "利润投产测算":
        page2.run()
    else:
        home.show()
