import os

from show_menu.show_help_menu import show_help_menu_function

def select_input_function(INPUT_FOLDER):
    width, upper_edge, middle_edge, lower_edge = show_help_menu_function()

    # --- Buscamos archivos Excel --- #
    try:
        input_files = [file for file in os.listdir(INPUT_FOLDER) if file.endswith(('.xlsx'))]

    except FileNotFoundError:
        # --- Si no existe la carpeta, informamos del error --- #
        print(f"\n⚠ Error: No existe la carpeta '{INPUT_FOLDER}'. Crea la carpeta o cambia la configuración")

        return None
        # --------------------------------- #
    # ------------------------------------------------------------------ #

    # --- Si no existen archivos dentro de la carpeta, informamos del error --- #
    if not input_files:
        print(f"\n⚠ Error: No se encontraron archivos de entrada en '{INPUT_FOLDER}'. Por favor añada tus ficheros Excel (.xlsx) en esa carpeta")

        return None
    # ------------------------------------------------------------------ #

    # --- Mostramos el menú --- #
    print("")
    print(upper_edge)
    print(f"║{('SELECCIÓN DE ARCHIVO DE ENTRADA').center(width)}║")
    print(f"║{('Carpeta: ' + INPUT_FOLDER).center(width)}║")
    print(middle_edge)
    
    # --- Escribimos cada uno de los archivos --- #
    for i, file in enumerate(input_files):
        idx = f"[{i + 1}]"
        linea = f"  {idx:<4} {file}"
        print(f"║{linea:<{width}}║")
    # --------------------------------- #
    
    print(middle_edge)
    print(f"║{("Escriba 'h' o 'help para mostrar la ayuda").center(width)}║")
    print(lower_edge)
    # ------------------------------------------------------------------ #

    # --- Selección de archivo de entrada --- #
    while True:
        try:
            # --- Obtenemos la opción elegida por el usuario --- #
            option = input("\n➤  Seleccione una opción: ")
            # --------------------------------- #
            
            # --- Terminamos la ejecución si el usuario así lo desea --- #
            if option.lower() in ['q', 'quit', 'exit']:
                return None, width, upper_edge, middle_edge, lower_edge
            # --------------------------------- #

            # --- Mostramos la ayuda si el usuario así lo desea --- #
            if option.lower() in ['h', 'help']:
                show_help_menu_function()
                
                continue
            # --------------------------------- #

            # --- Comprobamos si la opción elegida es correcta --- #
            idx = int(option) - 1

            if (0 <= idx < len(input_files)):
                file_selected = os.path.join(INPUT_FOLDER, input_files[idx])
                
                print(f"\tArchivo seleccionado: {input_files[idx]}\t\t✔")

                return file_selected, width, upper_edge, middle_edge, lower_edge
            else:
                print("\n\t⚠ Error: Opción fuera de rango. Inténtelo de nuevo")
            # --------------------------------- #
        except ValueError:
            print("\n\t⚠ Error: Entrada inválida. Ingrese un número que aparezca en la lista")
    # ------------------------------------------------------------------ #