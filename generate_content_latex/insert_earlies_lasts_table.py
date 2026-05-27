def insert_earlies_lasts_table_function(latex_content, ordered_tasks, earlies_formulas, lasts_formulas, project_duration):
    # --- Insertamos las filas iniciales y de apertura --- #
    latex_content.append("")
    latex_content.append("\\vspace{0.5cm}")
    latex_content.append("")
    latex_content.append(r"\textbf{Cálculo de Early y Last}")
    latex_content.append(r"\begin{table}")
    latex_content.append(r"\label{tab:tabla2}")
    latex_content.append(r"\centering")
    latex_content.append(r"\begin{tabular}{C|l}")
    latex_content.append(r"\toprule")
    latex_content.append(r"$T_i$ & $Earlies_i$ \\")
    latex_content.append(r"\midrule")
    # ------------------------------------------------------------------ #

    # --- Creamos distintas variables necesarias --- #
    total_tasks = len(ordered_tasks)
    # ------------------------------------------------------------------ #

    # --- Insertamos las filas para los earlies en la tabla ---- #
    for i, node in enumerate(ordered_tasks):
        earlies_text = earlies_formulas.get(node, "0")
        
        if ("=" in earlies_text): earlies_text = f"${earlies_text}$"
        
        latex_content.append(f"{node} & {earlies_text} \\\\")

        if (i < (total_tasks - 1)):
            latex_content.append(r"\hline")
        else:
            latex_content.append(r"\bottomrule")
            latex_content.append(r"\toprule")
    # ------------------------------------------------------------------ #

    # --- Insertamos un header intermedio para dividir los earlies de los lasts ---- #
    latex_content.append(r"$T_i$ & $Lasts_i$ \\")
    latex_content.append(r"\midrule")
    # ------------------------------------------------------------------ #

    # --- Insertamos las filas para los lasts en la tabla ---- #
    for i, node in enumerate(ordered_tasks):
        lasts_text = str(lasts_formulas.get(node, project_duration))

        if ("=" in lasts_text): lasts_text = f"${lasts_text}$"
        
        latex_content.append(f"{node} & {lasts_text} \\\\")

        if (i < (total_tasks - 1)):
            latex_content.append(r"\hline")
    # ------------------------------------------------------------------ #

    # --- Insertamos las filas de cierre ---- #
    latex_content.append(r"\bottomrule")
    latex_content.append(r"\end{tabular}")
    latex_content.append(r"\end{table} \\")
    # ------------------------------------------------------------------ #