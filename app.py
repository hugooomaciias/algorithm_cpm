import os
import base64
import pandas as pd
import streamlit as st

from cpm_algorithm import CPM_ALGORITHM
from translations import t

# ==========================================
# 1. PAGE CONFIGURATION & INITIALIZATION
# ==========================================

st.set_page_config(
    page_title="CPM Algorithm",
    page_icon="📊",
    layout="wide"
)

# Initialize Session State Variables
if 'cpm_executed' not in st.session_state:
    st.session_state.cpm_executed = False
if 'gantt_index' not in st.session_state:
    st.session_state.gantt_index = 0

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_FILENAME = "Template.xlsx"
INPUT_FOLDER = os.path.join(BASE_DIR, "INPUTS")
OUTPUT_FOLDER = os.path.join(BASE_DIR, "OUTPUTS")

os.makedirs(INPUT_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# ==========================================
# 2. SIDEBAR & LOCALIZATION
# ==========================================

with st.sidebar:
    st.header(":material/settings: Settings")
    idioma = st.selectbox(
        ":material/language: Select Language", 
        ["English", "Español"],
        index=0
    )

lang = t[idioma]

# ==========================================
# 3. MAIN UI: HEADER & INPUT HANDLING
# ==========================================

st.title(lang["title"])
st.markdown(lang["description"] + """---""")

st.header(f":material/input: {lang['input_title']}")

tab_example, tab_upload = st.tabs([
    f":material/folder: {lang['tab_example']}",
    f":material/upload: {lang['tab_upload']}"
])

input_file = None
input_identifier = ""

# Input Option A: Predefined Examples
with tab_example:
    st.markdown(lang['input_example_subtitle'])
    
    example_files = sorted([
        f for f in os.listdir(INPUT_FOLDER)
        if f.endswith((".xlsx", ".xls")) and f != TEMPLATE_FILENAME
    ])

    if example_files:
        selected_example = st.selectbox("Select an example", example_files, index=0, label_visibility="collapsed")
        example_input = os.path.join(INPUT_FOLDER, selected_example)
    else:
        st.warning("No example files found in the INPUTS folder.")
        example_input = None

# Input Option B: Custom File Upload
with tab_upload:
    st.markdown(lang['input_upload_subtitle'])

    # Botón de descarga de la plantilla
    template_path = os.path.join(INPUT_FOLDER, TEMPLATE_FILENAME)
    if os.path.exists(template_path):
        with open(template_path, "rb") as template_file:
            st.download_button(
                label=lang["btn_downlooad"],
                icon=":material/download:",
                data=template_file,
                file_name=TEMPLATE_FILENAME,
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
    else:
        st.error(f"Template file '{TEMPLATE_FILENAME}' not found.")
    
    # Subida de archivo
    uploaded_file = st.file_uploader(
        label=lang["upload_label"],
        type=["xlsx", "xls"]
    )

# Determine final input source
if uploaded_file is not None:
    input_file = uploaded_file
    input_identifier = uploaded_file.name
    st.info(f"{lang['input_upload_info']}**{uploaded_file.name}**")
elif example_input is not None:
    input_file = example_input
    input_identifier = selected_example
    st.info(f"{lang['input_example_info']}**{selected_example}**")

# ==========================================
# 4. PREVIEW DATA
# ==========================================

st.subheader(f":material/data_table: {lang['preview_title']}")

if input_file is not None:
    try:
        if 'current_preview_file' not in st.session_state or st.session_state.current_preview_file != input_identifier:  
            cpm_preview = CPM_ALGORITHM()
            st.session_state.tasks_preview = cpm_preview.upload_data(input_file)
            st.session_state.current_preview_file = input_identifier

        tasks_preview = st.session_state.tasks_preview

        formatted_rows = []
        for task_name, task_data in tasks_preview.items():
            successors = ", ".join(task_data['Sucessors']) if task_data['Sucessors'] else "-"

            formatted_rows.append({
                lang["preview_tasks"]: str(task_name),
                lang["preview_successors"]: successors,
                lang["preview_normal_duration"]: task_data['Normal Duration'],
                lang["preview_extreme_duration"]: task_data['Crash Duration'],
                lang["preview_normal_cost"]: f"{task_data['Normal Cost']} €",
                lang["preview_extreme_cost"]: f"{task_data['Crash Cost']} €",
                lang["preview_slope"]: task_data['Slope']
            })

        st.dataframe(pd.DataFrame(formatted_rows), use_container_width=True, hide_index=True)

    except Exception as e:
        st.warning(f"Could not load and format project data: {e}")
else:
    st.warning("Please select or upload a valid Excel file to preview data.")

# ==========================================
# 5. CORE EXECUTION LOGIC
# ==========================================

col1, col2, col3 = st.columns([2, 3, 2])

with col2:
    execute_button = st.button(
        f"**:material/route: {lang['run_btn']}**",
        use_container_width=True,
        type="primary",
        disabled=(input_file is None)
    )

if execute_button:
    try:
        with col2:
            with st.spinner(lang["run_loader"]):
                cpm = CPM_ALGORITHM()
                tasks = cpm.upload_data(input_file)
                cpm.manipulate_data()
                
                st.session_state.optimal_duration = cpm.optimal_duration
                st.session_state.optimal_cost = cpm.optimal_cost
                st.session_state.tasks = tasks
                st.session_state.cpm_executed = True
                st.session_state.gantt_index = 0 
            
    except Exception as e:
        st.error(f"Critical Error during execution: {e}")

# ==========================================
# 6. OUTPUT & VISUALIZATION
# ==========================================

if st.session_state.cpm_executed:
    try:
        tasks = st.session_state.tasks

        # Success Banner
        success_html = f"""
        <div style="background-color: #3DD56D33;
                padding: 15px; 
                border-radius: 8px; 
                text-align: center; 
                margin-bottom: 20px;">
            <span style="color: #5CE488; font-weight: bold; font-size: 16px;">
                {lang["run_success"]}
            </span>
        </div>
        """
        st.markdown(success_html, unsafe_allow_html=True)

        # Task Metrics
        st.markdown("---")
        st.subheader(f":material/assignment: {lang['tasks_title']}")

        total_tasks = len(tasks)
        critical_candidates = sum(1 for task in tasks.values() if task.get("Critical") == "Sí")

        metric_col1, metric_col2, metric_col3, metric_col4 = st.columns([1, 1, 1, 1])
        metric_col1.metric(lang["total_tasks"], total_tasks)
        metric_col2.metric(lang["critical_tasks"], critical_candidates)
        metric_col3.metric(lang["optimal_duration"], f"{st.session_state.optimal_duration} {lang['optimal_duration_unity']}")
        metric_col4.metric(lang["optimal_cost"], f"{st.session_state.optimal_cost:,.2f} €")

        # Static Visualizations
        col_graph, col_curve = st.columns(2)

        with col_graph:
            st.subheader(f"**:material/graph_4: {lang['dependency_graph']}**")
            graph_path = os.path.join(OUTPUT_FOLDER, "output_graph.png")
            if os.path.exists(graph_path):
                st.image(graph_path, use_container_width=True)
            else:
                st.warning("Graph image not found")

        with col_curve:
            st.subheader(f"**:material/show_chart: {lang['cost_time_curve']}**")
            curve_path = os.path.join(OUTPUT_FOLDER, "output_cost_curve.png")
            if os.path.exists(curve_path):
                st.image(curve_path, use_container_width=True)
            else:
                st.warning("Cost-Time curve not found")

        # Interactive Gantt Carousel
        st.subheader(f":material/align_horizontal_left: {lang['gantt_title']}")

        gantt_folder = os.path.join(OUTPUT_FOLDER, "OUTPUT_GANTT")

        if os.path.exists(gantt_folder):
            gantt_files = sorted([f for f in os.listdir(gantt_folder) if f.endswith(".png")])

            if gantt_files:
                def go_next():
                    st.session_state.gantt_index = (st.session_state.gantt_index + 1) % len(gantt_files)    
                def go_prev():
                    st.session_state.gantt_index = (st.session_state.gantt_index - 1) % len(gantt_files)

                col_prev, col_text, col_next = st.columns([1, 2, 1])
                
                with col_prev:
                    st.button(lang["previous_iter"], on_click=go_prev, use_container_width=True)
                
                with col_text:
                    current_file_name = gantt_files[st.session_state.gantt_index]
                    is_optimal = "(Optimo)" in current_file_name
                    
                    if is_optimal:
                        title_html = f"""
                        <div style='text-align: center;'>
                            <h4 style='color: #FFD700; margin-bottom: 0px;'>{lang['iter_title_optimal'].format(current=st.session_state.gantt_index + 1, total=len(gantt_files))}</h4>
                            <h5>{current_file_name}</h5>
                        </div>
                        """
                    else:
                        title_html = f"""
                        <div style='text-align: center;'>
                            <h4 style='color: #4CAF50; margin-bottom: 0px;'>{lang['iter_title'].format(current=st.session_state.gantt_index + 1, total=len(gantt_files))}</h4>
                            <h5>{current_file_name}</h5>
                        </div>
                        """
                    st.markdown(title_html, unsafe_allow_html=True)

                with col_next:
                    st.button(lang["next_iter"], on_click=go_next, use_container_width=True)

                image_path = os.path.join(gantt_folder, current_file_name)
                
                if os.path.exists(image_path):
                    if is_optimal:
                        with open(image_path, "rb") as img_file:
                            b64_img = base64.b64encode(img_file.read()).decode()
                            
                        html_code = f"""
                        <div style="border: 4px solid #FFD700; padding: 10px; border-radius: 10px; box-shadow: 0px 0px 15px rgba(255, 215, 0, 0.4);">
                            <img src="data:image/png;base64,{b64_img}" style="width: 100%;">
                        </div>
                        """
                        st.markdown(html_code, unsafe_allow_html=True)
                    else:
                        st.image(image_path, use_container_width=True)
                else:
                    st.error(f"No se pudo cargar la imagen: {current_file_name}")
            else:
                st.warning("No Gantt charts generated")
        else:
            st.warning(f"{gantt_folder} folder not found")

        # File Exports
        st.markdown("---")
        download_col1, download_col2, download_col3 = st.columns([2, 3, 2])
        
        with download_col2:
            st.subheader(f":material/inventory_2: {lang['export_title']}")

        latex_path = os.path.join(OUTPUT_FOLDER, "output_latex.tex")
        if os.path.exists(latex_path):
            with open(latex_path, "rb") as latex_file:
                download_col2.download_button(
                    label=lang["download_results"],
                    icon=":material/description:",
                    data=latex_file,
                    file_name="output_latex.tex",
                    mime="text/plain",
                    use_container_width=True,
                    type="primary"
                )

    except Exception as e:
        st.error(f"Critical Error displaying results: {e}")