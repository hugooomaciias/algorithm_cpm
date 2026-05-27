def insert_gantt_chart_function(tasks, latex_content, initial_project_duration):
    # --- Ponemos el título de la sección, abrimos la figura y el diagrama de Gantt indicando sus opciones --- #
    latex_content.append("")
    latex_content.append("\\vspace{0.5cm}")
    latex_content.append("")
    latex_content.append(r"\textbf{Diagrama de Gantt}")
    latex_content.append(r"\begin{figure}[h]")
    latex_content.append(r"\centering")
    latex_content.append(fr"\begin{{ganttchart}}[vgrid, x unit=0.8cm, y unit title=1cm, y unit chart=0.8cm, bar/.append style={{fill=Normal, draw=EdgeNormal, line width=1pt}}, bar height=0.6]{{0}}{{{initial_project_duration}}}")
    latex_content.append(fr"\gantttitlelist{{0 ,...,{initial_project_duration}}}{{1}} \\")
    # ------------------------------------------------------------------ #

    # --- Añadimos las barras para cada tarea --- #
    for task in tasks:
        start_time = tasks[task]['Early Start Node']
        normal_duration = tasks[task]['Normal Duration']
        current_duration = tasks[task]['Current Duration']

        normal_end_time = start_time + normal_duration - 1
        current_end_time = start_time + current_duration - 1

        if (tasks[task]['Critical'] == "No"):
            latex_content.append(f"\ganttbar[bar/.append style={{fill=Normal, draw=EdgeNormal, fill opacity=0.5}}]{{{task}}}{{{start_time}}}{{{normal_end_time}}}")
            latex_content.append(f"\ganttbar{{{task}}}{{{start_time}}}{{{current_end_time}}} \\\\")
        else:
            latex_content.append(f"\ganttbar[bar/.append style={{fill=Critical, draw=EdgeCritical, fill opacity=0.5}}]{{{task}}}{{{start_time}}}{{{normal_end_time}}}")
            latex_content.append(f"\ganttbar[bar/.append style={{fill=Critical, draw=EdgeCritical}}]{{{task}}}{{{start_time}}}{{{current_end_time}}} \\\\")
    # ------------------------------------------------------------------ #

    # --- Cerramos el diagrama de Gantt y la figura --- #
    latex_content.append(r"\end{ganttchart}")
    latex_content.append(r"\end{figure}")
    # ------------------------------------------------------------------ #
