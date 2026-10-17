import streamlit as st

def show():
    # 导航全局CSS，绘制深蓝色顶部导航栏
    st.markdown("""
    <style>
    .nav-container{
        background-color: #1f4e79;
        padding: 10px 20px;
        border-radius:4px;
        margin-bottom:20px;
    }
    /* 导航按钮样式覆盖 */
    div[data-testid="stHorizontalBlock"] .stButton>button {
        background-color:transparent;
        color:#ffffff;
        border:0;
        font-weight:700;
        font-size:16px;
        padding:6px 16px;
    }
    div[data-testid="stHorizontalBlock"] .stButton.active>button {
        background-color:#ffffff;
        color:#1f4e79;
        border-radius:6px;
    }
    </style>
    """, unsafe_allow_html=True)

    current_page = st.session_state.get("page", "首页")
    menu_list = ["首页", "线上编码工具", "利润投产测算"]

    # 创建横向列布局，用来模拟导航栏
    nav_cols = st.columns([0.12,0.16,0.18,0.58])

    # 首页
    with nav_cols[0]:
        is_active = (current_page == "首页")
        if is_active:
            st.markdown('<div class="stButton active">',unsafe_allow_html=True)
        if st.button("首页",key="nav_home"):
            st.session_state.page = "首页"
            st.rerun()
        if is_active:
            st.markdown('</div>',unsafe_allow_html=True)

    # 线上编码工具
    with nav_cols[1]:
        is_active = (current_page == "线上编码工具")
        if is_active:
            st.markdown('<div class="stButton active">',unsafe_allow_html=True)
        if st.button("线上编码工具",key="nav_code"):
            st.session_state.page = "线上编码工具"
            st.rerun()
        if is_active:
            st.markdown('</div>',unsafe_allow_html=True)

    # 利润投产测算
    with nav_cols[2]:
        is_active = (current_page == "利润投产测算")
        if is_active:
            st.markdown('<div class="stButton active">',unsafe_allow_html=True)
        if st.button("利润投产测算",key="nav_profit"):
            st.session_state.page = "利润投产测算"
            st.rerun()
        if is_active:
            st.markdown('</div>',unsafe_allow_html=True)

    # 退出登录，放在最右侧
    with nav_cols[3]:
        st.markdown('<div style="text-align:right">',unsafe_allow_html=True)
        if st.button("退出登录",key="nav_logout"):
            st.session_state.login_ok = False
            st.session_state.page = "首页"
            st.rerun()
        st.markdown('</div>',unsafe_allow_html=True)
