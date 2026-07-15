import streamlit as st

def metric_card(title, value, change):

    st.markdown(f"""
    <div class="metric-card">

        <div class="metric-title">
            {title}
        </div>

        <br>

        <div class="metric-value">
            {value}
        </div>

        <br>

        <div class="metric-change">
            {change}
        </div>

    </div>
    """, unsafe_allow_html=True)