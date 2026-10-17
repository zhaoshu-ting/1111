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

    st.title("利润投产测算")
    st.markdown("录入商品、成本、销售和投产信息，测算利润与投产效果。")

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="card-title">基础信息录入</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        product_name = st.text_input("商品名称")
        cost_price = st.number_input("成本价", min_value=0.0, step=0.01)
        sale_price = st.number_input("销售价", min_value=0.0, step=0.01)

    with col2:
        plan_qty = st.number_input("计划数量", min_value=0, step=1)
        put_cost = st.number_input("投产费用", min_value=0.0, step=0.01)
        other_cost = st.number_input("其他费用", min_value=0.0, step=0.01)

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="card-title">测算结果</div>', unsafe_allow_html=True)

    if st.button("开始测算", type="primary"):
        if sale_price > 0 and plan_qty > 0:
            revenue = sale_price * plan_qty
            profit = revenue - cost_price * plan_qty - put_cost - other_cost
            roi = profit / put_cost if put_cost > 0 else 0

            st.write(f"预计销售额：{revenue:.2f}")
            st.write(f"预计利润：{profit:.2f}")
            st.write(f"投产回报率：{roi:.2f}")

            if profit > 0:
                st.success("测算结果为盈利")
            else:
                st.warning("测算结果为亏损，请检查参数")
        else:
            st.warning("请完整输入销售价、计划数量等关键信息")

    st.markdown('</div>', unsafe_allow_html=True)
