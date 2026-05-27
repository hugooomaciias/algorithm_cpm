import streamlit as st
from cpm_algorithm import CPM_ALGORITHM

st.set_page_config(page_title="CPM Algorithm", layout="wide")

st.title("CPM Algorithm - Critical Path Method")

uploaded_file = st.file_uploader(
    "Upload Excel file",
    type=["xlsx", "xls"]
)

if uploaded_file:
    try:
        with st.spinner("Loading data..."):

            cpm = CPM_ALGORITHM()

            tasks = cpm.upload_data(uploaded_file)

        st.success("Data loaded successfully")

        st.subheader("Tasks")

        st.json(tasks)

        if st.button("Run CPM Algorithm"):

            with st.spinner("Executing algorithm..."):

                cpm.manipulate_data()

            st.success("Algorithm executed successfully")

            st.subheader("Generated Graph")

            st.image("OUTPUTS/output_graph.png")

            st.subheader("Cost-Time Curve")

            st.image("OUTPUTS/output_cost_curve.png")

            with open("OUTPUTS/output_latex.tex", "rb") as file:
                st.download_button(
                    "Download LaTeX Report",
                    file,
                    file_name="output_latex.tex"
                )

    except Exception as e:
        st.error(f"Critical Error: {e}")