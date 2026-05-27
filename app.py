import streamlit as st
from cpm_algorithm import CPM_ALGORITHM

st.set_page_config(page_title="CPM Algorithm", layout="wide")

st.title()("CPM Algorithm - Critical Path Method")

uploaded_file = st.file_uploader(
    "Upload Excel file",
    type=["xlsx", "xls"]
)

if uploaded_file is not None:
    st.success("File uploaded successfully!")
    
    try:
        cpm = CPM_ALGORITHM()

        st.info("Loading data...")

        tasks = cpm.upload_data(uploaded_file, 100)

        st.success("Data loaded successfully")

        st.write(tasks)

        if st.button("Run Algorithm"):

            st.info("Executing CPM algorithm...")

            cpm.manipulate_data()

            st.success("Algorithm executed successfully")

    except Exception as e:
        st.error(f"Critical Error: {e}")