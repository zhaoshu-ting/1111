import streamlit as st
import login
import nav
import home
import page1 #线上编码工具
import page2 #利润投产测算

st.set_page_config(page_title="发财工具箱", layout="wide")

#隐藏侧边栏
st.markdown("""
<style>
section[data-testid="stSidebar"]{
    display:none;
}
</style>
""",unsafe_allow_html=True)

#初始化session状态
if "login_ok" not in st.session_state:
    st.session_state.login_ok = False
if "page" not in st.session_state:
    st.session_state.page = "首页"

# DEBUG 放到这里，导入+初始化完成后
st.write("DEBUG 当前页面变量：", st.session_state.get("page"))
st.write("完整session：", st.session_state)

if not st.session_state.login_ok:
    login.show()
else:
    nav.show()
    # 路由
    if st.session_state.page == "首页":
        home.show()
    elif st.session_state.page == "线上编码工具":
        page1.show()
    elif st.session_state.page == "利润投产测算":
        page2.show()
    else:
        home.show()
