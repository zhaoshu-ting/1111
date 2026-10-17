import streamlit as st

st.set_page_config(layout="wide")

if "page" not in st.session_state:
    st.session_state.page = "首页"

menu = ["首页", "线上编码工具", "利润投产测算"]
nav_choice = st.radio("导航", menu, index=menu.index(st.session_state.page), horizontal=True)

if nav_choice != st.session_state.page:
    st.session_state.page = nav_choice
    st.rerun()

st.subheader(f"当前页面：{st.session_state.page}")
