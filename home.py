import streamlit as st

def show():
    st.markdown("""
    <style>
    .home-title {
        font-size: 26px;
        font-weight: 800;
        color: #111111;
        margin-top: 12px;
        margin-bottom: 8px;
    }
    .home-desc {
        font-size: 15px;
        color: #333333;
        margin-bottom: 24px;
    }
    .home-card {
        background: #ffffff;
        border: 1px solid #e5e7eb;
        border-radius: 16px;
        padding: 28px;
        box-shadow: 0 6px 18px rgba(0,0,0,0.06);
        cursor: pointer;
        transition: 0.2s;
    }
    .home-card:hover {
        border-color: #1f4e79;
        transform: translateY(-4px);
    }
    .home-card h3 {
        color: #111111;
        font-size: 20px;
        font-weight: 800;
    }
    .home-card p {
        color: #333333;
        font-size: 14px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="home-title">功能中心</div>', unsafe_allow_html=True)
    st.markdown('<div class="home-desc">选择下方功能卡片，进入对应业务模块。</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("线上编码工具", key="go_code"):
            st.session_state.page = "线上编码工具"
            st.rerun()

        st.markdown("""
        <div class="home-card">
            <h3>线上编码工具</h3>
            <p>上传线上商品表与成本价文件，按商品编码匹配并生成对应表格。</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        if st.button("利润投产测算", key="go_profit"):
            st.session_state.page = "利润投产测算"
            st.rerun()

        st.markdown("""
        <div class="home-card">
            <h3>利润投产测算</h3>
            <p>录入商品、成本、销售与投产信息，测算利润与投产效果。</p>
        </div>
        """, unsafe_allow_html=True)
