def calculate_slack_critical_path_function(tasks, earlies, lasts):
    # --- Calculamos la holgura y el camnio crítico --- #
    critical_path = []
    slack_content_latex = {}

    # --- Calculamos la holgura y añadimos tarea al camino crítico si no es una tarea ficticia --- #
    for task in tasks:
        predecessor_node = tasks[task]['Start Node']
        sucessor_node = tasks[task]['End Node']

        # --- Obtenemos diferentes parámetros de la tarea necesarios --- #
        duration = tasks[task]['Current Duration']
        critical = "No"
        # --------------------------------- #

        # --- Obtenemos el early del predecesor (i) y el last del sucesor (j) --- #
        early_predecessor_node = earlies[predecessor_node]
        last_successor_node = lasts[sucessor_node]
        # --------------------------------- #

        # --- Calculamos la holgura mediante la fórmula: last_j - duration - early_i --- #
        slack = last_successor_node - early_predecessor_node - duration
        # --------------------------------- #
        
        # --- Comprobamos si la tarea es crítica o no y la añadimos al camino crítico --- #
        if (abs(slack) == 0):
            critical = "Sí"
            critical_path.append(task)
        # --------------------------------- #

        tasks[task]['Slack'] = slack
        tasks[task]['Critical'] = critical

        # --- Añadimos la nueva línea a las lineas totales --- #
        slack_content_latex[task] = f"{task} & ${predecessor_node} \\rightarrow {sucessor_node}$ & {duration} & {early_predecessor_node} & {last_successor_node} & $H_{{ij}} = {last_successor_node} - {early_predecessor_node} - {duration} = {slack}$ & {critical}"
        # --------------------------------- # 
    # ------------------------------------------------------------------ #   

    critical_path_content_latex = " - ".join(critical_path)
    # ------------------------------------------------------------------ #        
    
    return critical_path, slack_content_latex, critical_path_content_latex