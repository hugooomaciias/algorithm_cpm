def create_gantt_chart_function(tasks, initial_project_duration):
    # --- Creamos la variable donde almacenaremos la información del diagrama --- #
    plot_data = []
    # ------------------------------------------------------------------ #

    # --- Obtenemos los instantes de inicio, fin y fin máximo para cada tarea --- #
    for task in tasks:
        # --- Obtenemos la duración de la tarea --- #
        normal_duration = tasks[task]['Normal Duration']
        current_duration = tasks[task]['Current Duration']
        # --------------------------------- #

        # --- Obtenemos el instante de inicio de la tarea --- #
        start_time = tasks[task]['Early Start Node']
        # --------------------------------- #
        
        # --- Obtenemos la holgura de la tarea --- #
        slack = tasks[task]['Slack']
        # --------------------------------- #

        # --- Obtenemos si la tarea es crítica o no --- #
        critical = tasks[task]['Critical']
        # --------------------------------- #

        # --- Guardamos la información del diagrama necesaria en la variable --- #
        plot_data.append({
            'label': task,
            'start': start_time,
            'normal_duration': normal_duration,
            'current_duration': current_duration,
            'project_duration': initial_project_duration,
            'slack': slack,
            'critical': critical
        })
        # --------------------------------- #
    # ------------------------------------------------------------------ #

    return plot_data