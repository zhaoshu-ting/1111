import streamlit as st

def show():
    # 导航栏原生容器
    nav_container = st.container()
    with nav_container:
        # 给这个容器设置深蓝色背景
        st.markdown("""
        <style>
        div[data-testid="stContainer"]:has(> div.nav-inner) {
            background-color: #1f4e79;
            padding: 10px 20px;
            border-radius:4px;
        }
        .nav-btn-normal > button {
            background: transparent;
            color: #ffffff;
            border: none;
            font-weight:700;
            font-size:16px;
            padding: 8px 18px;
        }
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

        st.markdown('<div class="nav-inner">', unsafe_allow_html=True)
        current_page = st.session_state.get("page", "首页")
        c1, c2, c3, c4 = st.columns([0.12,0.16,0.18,0.54])

        with c1:
            if current_page == "首页":
                st.markdown('<div class="nav-btn-active">', unsafe_allow_html=True)
            else:
                st.markdown('<div class="nav-btn-normal">', unsafe_allow_html=True)
            if st.button("首页", key="nav_home"):
                st.session_state.page = "首页"
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

        with c2:
            if current_page == "线上编码工具":
                st.markdown('<div class="nav-btn-active">', unsafe_allow_html=True)
            else:
                st.markdown('<div class="nav-btn-normal">', unsafe_allow_html=True)
            if st.button("线上编码工具", key="nav_code"):
                st.session_state.page = "线上编码工具"
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

        with c3:
            if current_page == "利润投产测算":
                st.markdown('<div class="nav-btn-active">', unsafe_allow_html=True)
            else:
                st.markdown('<div class="nav-btn-normal">', unsafe_allow_html=True)
            if st.button("利润投产测算", key="nav_profit"):
                st.session_state.page = "利润投产测算"
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

        with c4:
            st.markdown('<div class="nav-btn-normal" style="text-align:right;">', unsafe_allow_html=True)
            if st.button("退出登录", key="nav_logout"):
                st.session_state.login_ok = False
                st.session_state.page = "首页"
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
