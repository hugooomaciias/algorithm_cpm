import numpy as np

def generate_layers_function(tasks):
    # --- Creamos la variables necesarias para la creación de las columnas --- #
    layers = {}
    layer_count = 1
    first_node_second_layer = True
    first_node_next_layer = True
    terminal_node = None
    # ------------------------------------------------------------------ #

    # --- Ordenamos las tareas de menor a mayor Start Node --- #
    sorted_tasks = dict(sorted(tasks.items(), key=lambda item: item[1]['Start Node']))
    # ------------------------------------------------------------------ #

    # --- Definimos la primera columna, que siempre va a ser un único nodo (1) --- #
    layers[layer_count] = [1]
    layer_count += 1
    # ------------------------------------------------------------------ #

    # --- Definimos las columnas intermedias --- #
    for task in sorted_tasks:
        already_inserted_node = False

        start_node = tasks[task]['Start Node']
        end_node = tasks[task]['End Node']
        terminal = tasks[task]['Terminal']
        # --------------------------------- #

        if ((not terminal)):
            # --- Si la tarea no es terminal, la procesamos --- #
            if (start_node == 1):
                # --- Si su nodo inicial es el 1, esste nodo pertenece a la segunda columna --- #
                if (first_node_second_layer):
                    layers[layer_count] = []
                    first_node_second_layer = False
                # --------------------------------- #
            else:
                # --- Si tiene otro nodo inicial, pertenece a la tercera capa --- #
                # --- Comprobamos que no pertenezca a ninguna columna más --- #
                for layer in layers:
                    if (end_node in layers[layer]):
                        already_inserted_node = True

                        break
                # --------------------------------- #

                if (first_node_next_layer):
                    if (not already_inserted_node):
                        layer_count += 1
                        layers[layer_count] = []
                        first_node_next_layer = False
                    else:
                        continue
                # --------------------------------- #

            # --- Comprobamos que no este insertado en la columna actual o en la anterior --- #
            if ((end_node not in layers[layer_count]) and (end_node not in layers[layer_count - 1])):
                layers[layer_count].append(end_node)
            # --------------------------------- #
            # --------------------------------- #
        else:
            # --- Si la tarea es terminal, la guradamos para insertarla más tarde --- #
            terminal_node = end_node
            # --------------------------------- #
    # ------------------------------------------------------------------ #

    # --- Definimos la última columna (terminal_node) --- #
    layer_count += 1

    if (terminal_node not in layers[layer_count - 1]):
        layers[layer_count] = [terminal_node]
    # ------------------------------------------------------------------ #

    # --- Formateamos las columnas para poder usarlas en la creacion del fichero de salida del grafo --- #
    layers = list(layers.values())
    # ------------------------------------------------------------------ #

    return layers

def sort_key_function(n, graph, pos):
    # --- Calculamos la altura media de los padres --- #
    parents = [parent for parent in graph.predecessors(n) if (parent in pos)]
    avg_y = np.mean([pos[parent][1] for parent in parents]) if (parents) else 0
    # --------------------------------- #
    
    # --- Si hay conflicto, los ordenamos inversamente en base al nombre de la tarea --- #
    in_edge_label = 'z'

    for _, _, data in graph.in_edges(n, data=True):
        in_edge_label = str(data.get('label', 'z'))

        break
    # --------------------------------- #

    return (-avg_y, in_edge_label)