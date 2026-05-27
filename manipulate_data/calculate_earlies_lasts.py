def calculate_earlies_function(tasks, graph, ordered_nodes, earlies):
    # --- Calculamos los earlies --- #
    earlies_content_latex = {}

    for sucessor_node in ordered_nodes:
        terms_text = []
        terms_value = []

        for predecessor_node in graph.predecessors(sucessor_node):
            # --- Obtenemos la tarea que une ambos nodos --- #
            edge_data = graph[predecessor_node][sucessor_node]
            label = str(edge_data.get('label', ''))
            # --------------------------------- #
            
            # --- Calculamos la duración de la tarea --- #
            duration = 0

            if ('Fict' not in label):
                durations = []

                for tag in label:
                    if (tag in tasks):
                        d = tasks[tag].get('Current Duration', tasks[tag]['Normal Duration'])
                        durations.append(d)

                duration = max(durations) if (durations) else 0
            # --------------------------------- #

            # --- Asignar duración a la flecha en el grafo --- #
            graph[predecessor_node][sucessor_node]['calc_duration'] = duration
            # --------------------------------- #

            # --- Elegimos el máximo early --- #
            if ((earlies[predecessor_node] + duration) > earlies[sucessor_node]):
                earlies[sucessor_node] = earlies[predecessor_node] + duration
            # --------------------------------- #

            # --- Guardamos una nueva linea de texto y valores --- #
            terms_text.append(f"E_{predecessor_node} + {label}")
            terms_value.append(f"{earlies[predecessor_node]} + {duration}")
            # --------------------------------- #

            # --- Añadimos la nueva línea a las lineas totales --- #
            if (len(terms_text) == 1):
                # --- Un sólo camino para alcanzar el nodo --- #
                earlies_content_latex[sucessor_node] = f"{terms_text[0]} = {terms_value[0]} = {earlies[sucessor_node]}"
                # --------------------------------- #
            else:
                # --- Varios caminos para alcanzar el nodo --- #
                text_content = ", ".join(terms_text)
                value_content = ", ".join(terms_value)
                earlies_content_latex[sucessor_node] = f"\\max \\left\\{{ {text_content} \\right\\}} = "f"\\max \\left\\{{ {value_content} \\right\\}} = {earlies[sucessor_node]}"
                # --------------------------------- #
            # --------------------------------- #

    # --- Asignamos a cada tarea su información correspondiente sobre earlies --- #
    for task in tasks:
        start_node = tasks[task]['Start Node']
        end_node = tasks[task]['End Node']

        tasks[task]['Early Start Node'] = earlies[start_node]
        tasks[task]['Early End Node'] = earlies[end_node]

    project_duration = earlies[ordered_nodes[-1]]
    # --------------------------------- #
    # ------------------------------------------------------------------ #

    return earlies, project_duration, earlies_content_latex

def calculate_lasts_function(tasks, graph, ordered_nodes, lasts):
    lasts_content_latex = {}

    # --- Calculamos los lasts --- #
    for predecessor_node in reversed(ordered_nodes):
        terms_text = []
        terms_value = []

        for successor_node in graph.successors(predecessor_node):
            # --- Obtenemos la tarea que une ambos nodos --- #
            edge_data = graph[predecessor_node][successor_node]
            label = str(edge_data.get('label', ''))
            # --------------------------------- #

            # --- Obtenemos las duracion de la tarea --- #
            duration = graph[predecessor_node][successor_node]['calc_duration']
            # --------------------------------- #

            # --- Elegimos el mínimo last --- #
            if ((lasts[successor_node] - duration) < lasts[predecessor_node]):
                lasts[predecessor_node] = lasts[successor_node] - duration
            # --------------------------------- #

            # --- Guardamos una nueva linea de texto y valores --- #
            terms_text.append(f"L_{successor_node} - {label}")
            terms_value.append(f"{lasts[successor_node]} - {duration}")
            # --------------------------------- #

            # --- Añadimos la nueva línea a las lineas totales --- #
            if (len(terms_text) == 1):
                # --- Un sólo camino para alcanzar el nodo --- #
                lasts_content_latex[predecessor_node] = f"{terms_text[0]} = {terms_value[0]} = {lasts[predecessor_node]}"
                # --------------------------------- #
            else:
                # --- Varios caminos para alcanzar el nodo --- #
                text_content = ", ".join(terms_text)
                value_content = ", ".join(terms_value)
                lasts_content_latex[predecessor_node] = f"\\min \\left\\{{ {text_content} \\right\\}} = "f"\\min \\left\\{{ {value_content} \\right\\}} = {lasts[predecessor_node]}"
                # --------------------------------- #
            # --------------------------------- #

    # --- Asignamos a cada tarea su información correspondiente sobre earlies --- # 
    for task in tasks:
        start_node = tasks[task]['Start Node']
        end_node = tasks[task]['End Node']

        tasks[task]['Last Start Node'] = lasts[start_node]
        tasks[task]['Last End Node'] = lasts[end_node]
    # --------------------------------- #
    # ------------------------------------------------------------------ #

    return lasts, lasts_content_latex