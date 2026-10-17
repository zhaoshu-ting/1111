import streamlit as st

def show():
    # 只写背景样式，不操作按钮内部DOM，避免干扰点击
    st.markdown("""
    <style>
    .nav-bg {
        background-color: #1f4e79;
        padding: 10px 20px;
        border-radius: 4px;
    }
    /* 导航普通按钮样式 */
    .nav-btn-normal > button {
        background: transparent;
        color: #ffffff;
        border: none;
        font-weight:700;
        font-size:16px;
        padding: 8px 18px;
    }
    /* 当前激活页面按钮样式（白底深色字） */
    .nav-btn-active > button {
        background: #ffffff !important;
        color: #1f4e79 !important;
        border: none;
        font-weight:700;
        font-size:16px;
        padding: 8px 18px;
    }
    </style>
    """, unsafe_allow_html=True)

    current_page = st.session_state.get("page", "首页")
    # 外层放背景
    st.markdown('<div class="nav-bg">', unsafe_allow_html=True)
    # 导航横向列
    nav_cols = st.columns([0.12, 0.16, 0.18, 0.54])

    # 首页
    with nav_cols[0]:
        if current_page == "首页":
            st.markdown('<div class="nav-btn-active">', unsafe_allow_html=True)
        else:
            st.markdown('<div class="nav-btn-normal">', unsafe_allow_html=True)
        if st.button("首页", key="nav_home"):
            st.session_state.page = "首页"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    # 线上编码工具
    with nav_cols[1]:
        if current_page == "线上编码工具":
            st.markdown('<div class="nav-btn-active">', unsafe_allow_html=True)
        else:
            st.markdown('<div class="nav-btn-normal">', unsafe_allow_html=True)
        if st.button("线上编码工具", key="nav_code"):
            st.session_state.page = "线上编码工具"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    # 利润投产测算
    with nav_cols[2]:
        if current_page == "利润投产测算":
            st.markdown('<div class="nav-btn-active">', unsafe_allow_html=True)
        else:
            st.markdown('<div class="nav-btn-normal">', unsafe_allow_html=True)
        if st.button("利润投产测算", key="nav_profit"):
            st.session_state.page = "利润投产测算"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    # 退出登录
    with nav_cols[3]:
        st.markdown('<div class="nav-btn-normal" style="text-align:right;">', unsafe_allow_html=True)
        if st.button("退出登录", key="nav_logout"):
            st.session_state.login_ok = False
            st.session_state.page = "首页"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
