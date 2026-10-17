import streamlit as st

def run():
    st.markdown("""
    <style>
    .block-container {
        background: #ffffff;
    }
    h1, h2, h3 {
        color: #111111 !important;
    }
    p, div, label, span {
        color: #222222;
    }
    .card {
        background: #ffffff;
        border: 1px solid #e5e7eb;
        border-radius: 16px;
        padding: 24px;
        box-shadow: 0 4px 14px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
    .card-title {
        font-size: 18px;
        font-weight: 800;
        color: #111111;
        margin-bottom: 12px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.title("线上编码工具")
    st.markdown("上传线上商品表，按商品编码匹配成本价，生成A表和B表。")

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="card-title">线上商品表格</div>', unsafe_allow_html=True)
        st.info("必传，作为生成A表和B表的主文件。仅支持 .xlsx")
        file_online = st.file_uploader("点击或拖拽线上商品Excel到这里", type=["xlsx"], key="f1")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="card-title">成本价文件</div>', unsafe_allow_html=True)
        st.info("上传后会强校验，建议只读取商品id、档口名称、款号、成本价四列。")
        file_cost = st.file_uploader("点击或拖拽成本价Excel到这里", type=["xlsx"], key="f2")
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="card-title">款式类型</div>', unsafe_allow_html=True)
    style_type = st.radio("款式类型（加绒自动覆盖）", ["薄", "厚"], horizontal=True)
    st.caption("编码预览：常规：款式编码-厚-颜色-码数；加绒：款式编码-绒-颜色加绒-码数")
    st.markdown('</div>', unsafe_allow_html=True)

    run_btn = st.button("开始处理", type="primary")

    if run_btn:
        if file_online is None:
            st.warning("请先上传线上商品表格")
        elif file_cost is None:
            st.warning("请先上传成本价文件")
        else:
            st.success("文件已接收，准备进入编码处理逻辑。")

            # ========== 这里接你的原有功能代码 ==========
            # 例如：读取 df_online / df_cost
            # 按商品编码匹配
            # 生成 A表、B表
            # 输出下载按钮
            # ========== 示例占位 ==========
            st.write("线上商品表：", file_online.name)
            st.write("成本价文件：", file_cost.name)
            st.write("款式类型：", style_type)

    st.divider()

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="card-title">生成结果与下载</div>', unsafe_allow_html=True)
    st.info("处理完成后，A表和B表将在此区域展示并提供下载。")
    st.markdown('</div>', unsafe_allow_html=True)
