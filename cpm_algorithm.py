import networkx as nx
import os
import shutil

from upload_definition_data.upload_definition_data import upload_definition_data_function
from manipulate_data.manipulate_data import manipulate_data_function

# --- Carpeta y archivos de salida --- #
OUTPUT_FOLDER = 'OUTPUTS'

OUTPUT_GRAPH = os.path.join(OUTPUT_FOLDER, "output_graph.png")
OUTPUT_GANTT = os.path.join(OUTPUT_FOLDER, "OUTPUT_GANTT")
OUTPUT_LATEX = os.path.join(OUTPUT_FOLDER, "output_latex.tex")
OUTPUT_COST_TIME_CURVE = os.path.join(OUTPUT_FOLDER, "output_cost_curve.png")
# ------------------------------------------------------------------ #

class CPM_ALGORITHM:
    def __init__(self):
        self.latex_content = []
        self.tasks = {} 
        self.graph = nx.DiGraph()
        self.indirect_cost_A = 0
        self.indirect_cost_B = 0

    def upload_data(self, INPUT_FILE):
        # --- Borramos la carpeta anterior y creamos una carpeta para almacenar todos los archivos de salida --- #
        if os.path.exists(OUTPUT_FOLDER):
            shutil.rmtree(OUTPUT_FOLDER)

        os.makedirs(OUTPUT_FOLDER, exist_ok=True)
        # ------------------------------------------------------------------ #

        uploaded_data = upload_definition_data_function(INPUT_FILE, self.latex_content, self.tasks, self.graph, OUTPUT_GRAPH)

        self.indirect_cost_A = uploaded_data[0]
        self.indirect_cost_B = uploaded_data[1]

        return self.tasks

    def manipulate_data(self):

        manipulate_data_function(self, OUTPUT_GANTT, OUTPUT_COST_TIME_CURVE)

        # --- Escribimos el contenido en LaTex --- #
        with open(OUTPUT_LATEX, 'w', encoding='utf-8') as f:
            f.write("\n".join(self.latex_content))
        # ------------------------------------------------------------------ #