def insert_duration_costs_table_function(latex_content, tasks):
    # --- Insertamos las filas iniciales y de apertura --- #
    latex_content.append("")
    latex_content.append("\\vspace{0.5cm}")
    latex_content.append("")
    latex_content.append(r"\textbf{Tabla de duraciones y costes}")
    latex_content.append(r"\begin{table}")
    latex_content.append(r"\label{tab:tabla1}")
    latex_content.append(r"\centering")
    latex_content.append(r"\begin{tabular}{C|CCCCC}")
    latex_content.append(r"\toprule")
    latex_content.append(r"Actividad & Duracion (días) & Duración Extrema (días) & Coste (\euro) & Coste Extremo (días) & Slope \\")
    latex_content.append(r"\midrule")
    # ------------------------------------------------------------------ #

    # --- Insertamos una fila de la tabla por cada tarea --- #
    for task in tasks:
        duration = tasks[task]['Current Duration']
        crash_duration = tasks[task]['Crash Duration']
        cost = tasks[task]['Current Cost']
        crash_cost = tasks[task]['Crash Cost']
        slope = tasks[task]['Slope']

        new_table_line = f"{task} & {duration} & {crash_duration} & {cost} & {crash_cost} & {slope} \\\\"
        latex_content.append(new_table_line)
    # ------------------------------------------------------------------ #

    # --- Insertamos las filas de cierre ---- #
    latex_content.append(r"\bottomrule")
    latex_content.append(r"\end{tabular}")
    latex_content.append(r"\end{table} \\")
    # ------------------------------------------------------------------ #