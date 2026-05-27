import pandas as pd

from generate_content_latex.insert_dependencies import insert_dependencies_function

def prepare_graph_function(latex_content, tasks, input_data, idx_dependencies, tasks_ids):
    # --- Obtenemos las dependencias --- #
    idx_dependencies_start = idx_dependencies + 1
    mapped_tasks = {i + 1: tid for i, tid in enumerate(tasks_ids)}
    # ------------------------------------------------------------------ #

    # --- Obtenemos todos los precedecedores y sucesores --- #
    for r in range(idx_dependencies_start, len(input_data)):
        row_data = input_data.iloc[r]

        predecessor_id = row_data[0]

        if ((pd.isna(predecessor_id)) or (predecessor_id not in tasks_ids)):
            continue
        
        for column_idx, value in row_data.items():
            if ((column_idx in mapped_tasks) and (value == 1)):
                sucessor_id = mapped_tasks[column_idx]

                tasks[sucessor_id]['Predecessors'].append(predecessor_id)
                tasks[predecessor_id]['Sucessors'].append(sucessor_id)
    # ------------------------------------------------------------------ #

    # --- Insertamos las dependencias en el fichero LaTex --- #
    insert_dependencies_function(latex_content, tasks)
    # ------------------------------------------------------------------ #