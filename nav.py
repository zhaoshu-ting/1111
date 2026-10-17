import streamlit as st

def show():
    # 导航栏CSS，外观完全不变，深蓝色顶栏
    st.markdown("""
    <style>
    .nav-wrap {
        background-color: #1f4e79;
        padding: 8px 20px;
        border-radius:4px;
        display:flex;
        align-items:center;
        gap:8px;
    }
    .nav-btn > button{
        background:transparent !important;
        color:white !important;
        border:none !important;
        font-weight:700;
        font-size:16px;
        padding:6px 16px;
        height:auto;
    }
    .nav-btn.active > button{
        background-color:#ffffff !important;
        color:#1f4e79 !important;
        border-radius:6px;
    }
    .nav-logout{
        margin-left:auto;
    }
    </style>
    """, unsafe_allow_html=True)

    menus = ["首页", "线上编码工具", "利润投产测算"]
    current_page = st.session_state.get("page", "首页")

    st.markdown('<div class="nav-wrap">', unsafe_allow_html=True)
    # 循环渲染导航按钮
    for menu_name in menus:
        active_class = "nav-btn active" if menu_name == current_page else "nav-btn"
        with st.container():
            st.markdown(f'<div class="{active_class}">', unsafe_allow_html=True)
            if st.button(menu_name, key=f"nav_{menu_name}"):
                st.session_state.page = menu_name
                st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)

    # 退出登录
    with st.container():
        st.markdown('<div class="nav-btn nav-logout">', unsafe_allow_html=True)
        if st.button("退出登录", key="nav_logout"):
            st.session_state.login_ok = False
            st.session_state.page = "首页"
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
