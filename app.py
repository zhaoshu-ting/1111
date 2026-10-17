import streamlit as st
import login
import nav
import home
import page1
import page2

st.set_page_config(page_title="发财工具箱", layout="wide")

# 隐藏侧边栏 + 美化radio为深蓝色标签样式
st.markdown("""
<style>
section[data-testid="stSidebar"]{
    display:none;
}
/* 把radio改成顶部深蓝色标签效果 */
div[class*="stRadio"] > label > div[data-testid="stMarkdownContainer"] {
    display:none;
}
div[class*="stRadio"] {
    background-color:#1f5699;
    padding:8px 16px;
    border-radius:6px;
}
div[class*="stRadio"] label {
    color:white !important;
    font-weight:bold;
    padding:6px 14px !important;
    border-radius:4px;
}
div[class*="stRadio"] label[data-checked="true"]{
    background-color:white !important;
    color:#1f5699 !important;
}
</style>
""",unsafe_allow_html=True)

#初始化session
if "login_ok" not in st.session_state:
    st.session_state.login_ok = False
if "page" not in st.session_state:
    st.session_state.page = "首页"

if not st.session_state.login_ok:
    login.show()
else:
    nav.show()
    #页面路由
    if st.session_state.page == "首页":
        home.show()
    elif st.session_state.page == "线上编码工具":
        page1.show()
    elif st.session_state.page == "利润投产测算":
        page2.show()
    else:
        home.show()
