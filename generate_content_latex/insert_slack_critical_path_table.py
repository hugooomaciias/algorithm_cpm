def insert_slack_critical_path_table_function(tasks, latex_content, slack_content_latex, critical_path_content_latex, project_duration):
    # --- Insertamos las filas iniciales y de apertura --- #
    latex_content.append("")
    latex_content.append(r"\newpage")
    latex_content.append("")
    latex_content.append(r"\textbf{Cálculo de la holgura y el camino crítico}")
    latex_content.append(r"\begin{table}")
    latex_content.append(r"\label{tab:tabla3}")
    latex_content.append(r"\centering")
    latex_content.append(r"\begin{tabular}{C|CCCCcC}")
    latex_content.append(r"\toprule")
    latex_content.append(r"Tarea & Ruta($i \rightarrow j$) & $Duracion_{ij}$ & $Early_i$ & $Last_j$ & $Holgura_{ij} = Last_j - Early_i - Duracion_{ij}$ & Crítica \\")
    latex_content.append(r"\midrule")
    # ------------------------------------------------------------------ #

    # --- Insertamos las filas para cada tarea en la tabla ---- #
    for task in tasks:
        latex_content.append(f"{slack_content_latex[task]} \\\\")
    # ------------------------------------------------------------------ #

    # --- Insertamos las filas de cierre ---- #
    latex_content.append(r"\bottomrule")
    latex_content.append(r"\end{tabular}")
    latex_content.append(r"\end{table}")
    # ------------------------------------------------------------------ #

    # --- Añadimos los apartados de camino crítico y duración del proyecto --- #
    latex_content.append(r"")
    latex_content.append(r"\begin{multicols}{2}")
    latex_content.append(r"\textbf{Camino crítico:}")
    latex_content.append(r"")
    latex_content.append(f"{critical_path_content_latex}")
    latex_content.append(r"")
    latex_content.append(r"\textbf{Duración del proyecto:}")
    latex_content.append(r"")
    latex_content.append(f"{project_duration}")
    latex_content.append(r"\end{multicols}")
    # ------------------------------------------------------------------ #