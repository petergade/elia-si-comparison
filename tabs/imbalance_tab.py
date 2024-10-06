import streamlit as st

def render_imbalance_tab():
    st.header('Imbalance API Comparison')

    grid_data_col, open_data_col = st.columns(2)

    with grid_data_col:
        st.write('data from GridData api')

    with open_data_col:
        st.write('data from OpenData api')