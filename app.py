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
