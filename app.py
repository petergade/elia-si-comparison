import streamlit as st
from tabs.imbalance_tab import render_imbalance_tab
from tabs.imbalance_price_tab import render_imbalance_price_tab

imbalanceTab, imbalancePriceTab = st.tabs(['Imbalance', 'Imbalance Price'])

with imbalanceTab:
     render_imbalance_tab()

with imbalancePriceTab:
    render_imbalance_price_tab()