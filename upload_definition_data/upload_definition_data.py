import pandas as pd

from upload_definition_data.prepare_graph import prepare_graph_function
from upload_definition_data.create_graph import create_graph_function
from upload_definition_data.generate_output_graph import generate_output_graph_function

from generate_content_latex.insert_preamble import insert_preamble_function
from generate_content_latex.insert_graph import insert_graph_function

def upload_definition_data_function(INPUT_FILE, latex_content, tasks, graph, OUTPUT_GRAPH):
    # --- Insertamos todo el preámbulo y las líneas iniciales en Latex --- #
    insert_preamble_function(latex_content)
    # ------------------------------------------------------------------ #

    # --- Leemos el Excel desde la entrada proporcionada --- #
    input_data = pd.read_excel(INPUT_FILE, header=None)
    # ------------------------------------------------------------------ #

    # --- Obtenemos los índices de las diferentes secciones --- #
    idx_duration = input_data[input_data[0].astype(str).str.contains("Duración", case=False, na=False)].index[0]
    idx_costs = input_data[input_data[0].astype(str).str.contains("Costes", case=False, na=False)].index[0]
    idx_indirect_costs = input_data[input_data[0].astype(str).str.contains("Costes indirectos", case=False, na=False)].index[0]
    idx_dependencies = input_data[input_data[0].astype(str).str.contains("Dependencias", case=False, na=False)].index[0]
    # ------------------------------------------------------------------ #

    # --- Obtenemos las tareas definidas en el excel --- #
    header_row = input_data.iloc[idx_duration]
    tasks_ids = [x for x in header_row.values[1:] if str(x) != 'nan']
    # ------------------------------------------------------------------ #

    # --- Obtenemos los datos de las duraciones --- #
    row_normal_duration = input_data.iloc[idx_duration + 1, 1:len(tasks_ids)+1].values
    row_crash_duration = input_data.iloc[idx_duration + 2, 1:len(tasks_ids)+1].values
    # ------------------------------------------------------------------ #

    # --- Obtenemos los datos de los costes --- #
    row_normal_costs = input_data.iloc[idx_costs + 1, 1:len(tasks_ids)+1].values
    row_crash_costs = input_data.iloc[idx_costs + 2, 1:len(tasks_ids)+1].values
    # ------------------------------------------------------------------ #

    # --- Realizamos una copia de la lista para poder modificarla y recorrerla al mismo tiempo --- #
    tasks_ids_complete = tasks_ids.copy()
    # ------------------------------------------------------------------ #

    # --- Almacenamos las tareas con sus respectivos valores de duraciones, costes y slope --- #
    for i, tid in enumerate(tasks_ids_complete):
        # --- Si la tarea no tiene duracion ni coste asociado la eliminamos --- #
        if ((pd.isna(row_normal_duration[i])) and (pd.isna(row_normal_costs[i]))):
            tasks_ids.remove(tid)
            continue
        # --------------------------------- #

        # --- Calculamos duraciones y costes --- #
        normal_duration = int(row_normal_duration[i]) if (pd.notna(row_normal_duration[i])) else 0
        crash_duration = int(row_crash_duration[i]) if (pd.notna(row_crash_duration[i])) else normal_duration
        normal_costs = int(row_normal_costs[i]) if (pd.notna(row_normal_costs[i])) else 0
        crash_costs = int(row_crash_costs[i]) if (pd.notna(row_crash_costs[i])) else normal_costs
        # --------------------------------- #

        # --- Calculamos pendiente de coste (Slope) --- #
        if (normal_duration > crash_duration):
            slope = (crash_costs - normal_costs) / (normal_duration - crash_duration)
            slope = round(slope, 2)
        else:
            slope = float('inf')
        # --------------------------------- #

        # --- Almacenamos valores calculados --- #
        tasks[tid] = {
            'Normal Duration': normal_duration, 'Crash Duration': crash_duration, 'Current Duration': normal_duration,
            'Normal Cost': normal_costs, 'Crash Cost': crash_costs, 'Current Cost': normal_costs, 'Slope': slope,
            'Predecessors': [], 'Sucessors': [], 'Start Node': None, 'End Node': None, 'Terminal': False,
            'Early Start Node': None, 'Last Start Node': None, 'Early End Node': None, 'Last End Node': None,
            'Slack': None, 'Critical': None
        }
        # --------------------------------- #
    # ------------------------------------------------------------------ #

    # --- Obtenemos los costes indirectos mediante la fórmula 'A + B * X(Duración camino crítico)' --- #
    indirect_cost_A = int(input_data.iloc[idx_indirect_costs + 1, 1]) if (input_data.iloc[idx_indirect_costs + 1, 1]) else 0
    indirect_cost_B = int(input_data.iloc[idx_indirect_costs + 1, 2]) if (input_data.iloc[idx_indirect_costs + 1, 2]) else 0
    # ------------------------------------------------------------------ #

    # --- Preparamos el grafo para construirlo --- #
    prepare_graph_function(latex_content, tasks, input_data, idx_dependencies, tasks_ids)
    # ------------------------------------------------------------------ #

    # --- Construimos el grafo --- #
    create_graph_function(tasks, graph)
    # ------------------------------------------------------------------ #

    # --- Generamos el fichero de salida que contiene el grafo --- #
    generate_output_graph_function(tasks, graph, OUTPUT_GRAPH)
    # ------------------------------------------------------------------ #

    # --- Insertamos el grafo en el fichero LaTex --- #
    insert_graph_function(latex_content, OUTPUT_GRAPH)
    # ------------------------------------------------------------------ #

    return indirect_cost_A, indirect_cost_B