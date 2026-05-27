def show_help_menu_function():
    # --- Definimos los comandos que queremos mostrar en la ayuda --- #
    commands = [
        ("[Nº]", "Selecciona el archivo correspondiente a Nº"),
        ("q/quit/exit", "Cierra la aplicación inmediatamente"),
        ("h/help", "Muestra este menú de ayuda"),
    ]
    # ------------------------------------------------------------------ #

    # --- Definimos la información adicional que queremos mostrar en la ayuda --- #
    info_lines = [
        "» Los archivos deben estar en la carpeta: INPUTS",
        "» El formato admitido es EXCEL (.xlsx)",
        "» Asegúrate de que el Excel sigue la plantilla",
    ]
    # ------------------------------------------------------------------ #

    # --- Calculamos el ancho dinámicamente --- #
    # --- Establecemos el espaciado interno --- #
    padding = 4
    # --------------------------------- #
    
    # --- Calculamos el comando + descripción más ancho --- #
    max_cmd_width = max(len(command[0]) for command in commands) + 3
    max_commands_width = max(max_cmd_width + len(command[1]) for command in commands)
    # --------------------------------- #
    
    # --- Calculamos la información adicional más ancho --- #
    max_info_width = max(len(line) for line in info_lines)
    # --------------------------------- #

    # --- Calculamos el ancho maximo para asignar a todas las lineas --- #
    width = max(max_commands_width, max_info_width) + padding
    # --------------------------------- #
    # ------------------------------------------------------------------ #

    # --- Establecemos los limites del menú --- #
    upper_edge = "╔" + "═" * (width) + "╗"
    middle_edge = "╠" + "═" * (width) + "╣"
    lower_edge = "╚" + "═" * (width) + "╝"
    # --------------------------------- #
    
    # --- Escribimos los comandos --- #
    for command, description in commands:
        line = f" {command:<{max_cmd_width}}{description}" 
    # --------------------------------- #
    # ------------------------------------------------------------------ #

    return width, upper_edge, middle_edge, lower_edge