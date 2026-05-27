def create_graph_function(tasks, graph):
    # --- Añadimos el primer nodo al grafo --- #
    graph.add_node(1)
    # ------------------------------------------------------------------ #

    # --- Creamos la variables necesarias para la creación del grafo --- #
    node_counter = 1
    dummies_counter = 1
    task_end_nodes = {}
    terminal_node = None
    first_terminal_task = True
    # ------------------------------------------------------------------ #

    # --- Creación del grafo --- #
    for task in tasks:
        predecessors = tasks[task]['Predecessors']

        start_node = None
        
        # --- Establecemos el nodo inicial de cada tarea --- #
        if (not predecessors):
            # --- Si no tiene predecesores, su nodo inicial es el primer nodo --- #
            start_node = 1
            # --------------------------------- #
        else:
            # --- Si tiene predecesores, buscamos que nodo será su inicial --- #
            # --- Obtenemos los nodos en los que terminan los predecesores --- #
            predecessors_end_nodes = []

            for predecessor in predecessors:
                if (predecessor in task_end_nodes):
                    predecessors_end_nodes.append(task_end_nodes[predecessor])

            predecessors_end_nodes = sorted(list(predecessors_end_nodes))
            # --------------------------------- #

            if (len(set(predecessors_end_nodes)) == 1):
                # --- Si solo tiene un predecesor o todos los predecesores acaban en el mismo nodo --- #
                start_node = predecessors_end_nodes[0]
                # --------------------------------- #
            else:
                # --- Si tiene varios predecesores, creamos una tarea ficticia desde el que más sucesores tiene al que menos --- #
                minimum_length = float('inf')
                less_successors_task = None

                for predecessor in predecessors:
                    successors = tasks[predecessor]['Sucessors']

                    if (len(successors) < minimum_length):
                        minimum_length = len(successors)
                        less_successors_task = predecessor

                node_dch = task_end_nodes[less_successors_task]
                source_nodes = [node for node in predecessors_end_nodes if node != node_dch]

                for node_izq in source_nodes:
                    if (not graph.has_edge(node_izq, node_dch)):
                        graph.add_edge(node_izq, node_dch, label=f"Fict_{dummies_counter}", style='dashed', duration=0)

                        dummies_counter = dummies_counter + 1

                start_node = node_dch
                # --------------------------------- #
            # --------------------------------- #
        # --------------------------------- #

        # --- Creamos y establecemos el nodo final de cada tarea --- #
        successors = tasks[task]['Sucessors']

        # --- Obtenemos si la tarea es terminal o no --- #
        terminal = False

        if ((len(successors) == 0) and (not terminal_node)):
            terminal = True
        # --------------------------------- #

        if (terminal):
            # --- Si es un nodo terminal --- #
            if (first_terminal_task):
                node_counter += 1
                terminal_node = node_counter
                graph.add_node(terminal_node)

                first_terminal_task = False 
            
            end_node = terminal_node

            tasks[task]['Terminal'] = True
            # --------------------------------- #
        else:
            # --- Si no es un nodo terminal --- #
            reused_node = None

            # --- Obtenemos si se debe reusar algún nodo final --- #
            for prev_task in task_end_nodes:
                if ((task_end_nodes[prev_task] != (node_counter + 1)) and (tasks[prev_task]['Sucessors'] == successors)):
                    reused_node = task_end_nodes[prev_task]

                    break
            # --------------------------------- #

            if (reused_node):
                end_node = reused_node
            else:
                node_counter += 1
                end_node = node_counter
                graph.add_node(end_node)
            # --------------------------------- #

        task_end_nodes[task] = end_node
        # --------------------------------- #

        # --- Unimos los diferentes nodos mediante las aristas --- #
        actual_end_node = end_node

        if (graph.has_edge(start_node, end_node)):
            # --- Si hay conflicto dibujamos un nodo adicional y añadimos una tarea ficticia --- #
            node_counter += 1
            intermediate_node = node_counter
            graph.add_node(intermediate_node)

            graph.add_edge(start_node, intermediate_node, label=task, style='solid')
            
            graph.add_edge(intermediate_node, end_node, label=f"Fict_{dummies_counter}", style='dashed', duration=0)
            
            dummies_counter += 1
            
            actual_end_node = intermediate_node
            # --------------------------------- #
        else:
            # --- Si no hay ningún conflicto, dibujamos la flecha directamente --- #
            graph.add_edge(start_node, end_node, label=task, style='solid')
            # --------------------------------- #
        # --------------------------------- #

        # --- Guardamos el nodo de inicio y fin de cada tarea --- #
        tasks[task]['Start Node'] = start_node
        tasks[task]['End Node'] = actual_end_node
        # --------------------------------- #
    # ------------------------------------------------------------------ #