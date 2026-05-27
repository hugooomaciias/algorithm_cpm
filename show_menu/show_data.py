def show_data_function(tasks):
    # --- Definimos las cabeceras --- #
    headers = [
        "Tarea", 
        "Sucesores", 
        "Duración Normal", 
        "Duración Extrema", 
        "Coste Normal", 
        "Coste Extremo", 
        "Slope"
    ]
    # ------------------------------------------------------------------ #

    # --- Obtenemos todas las filas que vamos a insertar en la tabla --- #
    rows = []

    for task in tasks:
        # --- Obtenemos los sucesores de cada tarea --- #
        successors = ", ".join(tasks[task]['Sucessors']) if (tasks[task]['Sucessors']) else "-"
        # --------------------------------- #

        # --- Añadimos una fila por cada tarea --- #
        rows.append([
            str(task),
            successors,
            str(tasks[task]['Normal Duration']),
            str(tasks[task]['Crash Duration']),
            f"{tasks[task]['Normal Cost']} €",
            f"{tasks[task]['Crash Cost']} €",
            str(tasks[task]['Slope'])
        ])
        # --------------------------------- #
    # ------------------------------------------------------------------ #

    # --- Calculamos el ancho de cada columna según su header correspondiente --- #
    widths = []

    for i in range(len(headers)):
        # --- Obtenemos la longitud del header y el de cada uno de las filas para esa columna --- #
        header_length = len(headers[i])
        max_data_length = max([len(row[i]) for row in rows]) if (rows) else 0
        # --------------------------------- #
        
        # --- Añadimos el ancho que tendrá la columna, que será el máximo entre la longitud del header y su fila más larga --- #
        widths.append(max(header_length, max_data_length) + 2)
        # --------------------------------- #
    # ------------------------------------------------------------------ #

    # --- Obtenemos el ancho total de la tabla --- #
    total_width = sum(widths) + (len(widths) - 1)
    # ------------------------------------------------------------------ #

    # --- Definimos los bordes y separadores de la tabla --- #
    upper_edge = "\t" + "╔" + "═".join([("═" * width) for width in widths]) + "╗"
    middle_edge = "\t" + "╠" + "╦".join([("═" * width) for width in widths]) + "╣"
    middle_table_edge = "\t" + "╠" + "╬".join([("═" * width) for width in widths]) + "╣"
    lower_edge = "\t" + "╚" + "╩".join([("═" * width) for width in widths]) + "╝"
    # ------------------------------------------------------------------ #

    # --- Dibujamos la tabla --- #

    # --- Insertamos todos los headers --- #
    header_row = "\t║" + "║".join([(header.center(width)) for header, width in zip(headers, widths)]) + "║"
    # --------------------------------- #

    # --- Insertamos cada uno de las filas de datos --- #
    for row in rows:
        data_row = "\t║" + "║".join([(data.center(width)) for data, width in zip(row, widths)]) + "║"
    # --------------------------------- #
    # ------------------------------------------------------------------ #