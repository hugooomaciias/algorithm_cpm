def insert_project_cost_function(latex_content, costs_content_latex):
    # --- Añadimos los apartados de camino crítico y duración del proyecto --- #
    latex_content.append("")
    latex_content.append("\\vspace{0.5cm}")
    latex_content.append("")
    latex_content.append(r"\textbf{Coste del proyecto}")
    latex_content.append(r"")
    latex_content.append(f"{costs_content_latex}")
    # ------------------------------------------------------------------ #