import streamlit as st

def show():
    st.markdown("""
    <style>
    .top-nav {
        background-color: #1f4e79;
        padding: 0 24px;
        display: flex;
        align-items: center;
        height: 56px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    }
    .nav-item {
        color: #ffffff;
        font-size: 16px;
        font-weight: 700;
        padding: 10px 18px;
        margin-right: 6px;
        border-radius: 8px;
        cursor: pointer;
    }
    .nav-item:hover {
        background-color: #2b6ca3;
    }
    .nav-active {
        background-color: #ffffff;
        color: #1f4e79 !important;
    }
    .nav-logout {
        margin-left: auto;
    }
    </style>
    """, unsafe_allow_html=True)

    menus = ["首页", "线上编码工具", "利润投产测算"]
    current = st.session_state.get("page", "首页")

    nav_html = '<div class="top-nav">'
    for m in menus:
        active = "nav-active" if m == current else ""
        nav_html += f'<div class="nav-item {active}" onclick="window.location.href=\'?page={m}\'">{m}</div>'
    nav_html += '<div class="nav-item nav-logout" onclick="window.location.href=\'?logout=1\'">退出登录</div>'
    nav_html += '</div>'

    st.markdown(nav_html, unsafe_allow_html=True)
