def insert_dependencies_function(latex_content, tasks):
    # --- Insertamos una primera columna con las dependencias --- #
    latex_content.append(r"")
    latex_content.append(r"\textbf{Precedencia de actividades} \\")

    for task in tasks:
        for sucessor in tasks[task]['Sucessors']:
            latex_content.append(f"${task} \\rightarrow {sucessor}$ \\\\")
    # ------------------------------------------------------------------ #