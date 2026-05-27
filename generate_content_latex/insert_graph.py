import os

def insert_graph_function(latex_content, OUTPUT_GRAPH):
    # --- Ponemos el título de la columna y abrimos el grafo indicando sus opciones --- #
    latex_content.append(r"")
    latex_content.append(r"\vspace{0.5cm}")
    latex_content.append(r"")
    latex_content.append(r"\textbf{Grafo} \\")
    latex_content.append(r"\vspace{-0.8cm}")
    # ------------------------------------------------------------------ #

    # --- Obtenemos solo el nombre del fichero sin la carpeta --- #
    filename = os.path.basename(OUTPUT_GRAPH)
    # ------------------------------------------------------------------ #

    # --- Cerramos la figura --- #
    latex_content.append(r"\begin{figure}")
    latex_content.append(r"\centering")
    latex_content.append(f"\\includegraphics[width=0.95\\linewidth]{{{filename}}}")
    latex_content.append(r"\end{figure}")
    latex_content.append(r"\end{center}")
    # ------------------------------------------------------------------ #