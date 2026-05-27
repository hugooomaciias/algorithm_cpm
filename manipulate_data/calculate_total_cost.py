def calculate_total_cost_function(tasks, indirect_cost_A, indirect_cost_B, project_duration):
    # --- Creamos las variables necesarias --- #
    total_cost = 0
    costs_text_content_latex = []
    costs_value_content_latex = []
    # ------------------------------------------------------------------ #

    # --- Calculamos el coste directo total y lo añadimos a las listas --- #
    direct_cost = 0

    for task in tasks:
        task_cost = tasks[task].get('Current Cost')

        costs_text_content_latex.append(f"{task} ({task_cost}\\euro)")
        costs_value_content_latex.append(str(task_cost))

        direct_cost += task_cost
    # ------------------------------------------------------------------ #

    # === Checkpoint para ver el punto en el que se encuentra la ejecución === #
    print("\t\t\t\t» Coste directo del proyecto calculado")
    # ================================================================== #

    # --- Calculamos el coste indirecto total y lo añadimos a las listas --- #
    indirect_cost = indirect_cost_A + (indirect_cost_B * project_duration)

    costs_text_content_latex.append(f"({indirect_cost_A}\\euro + ({indirect_cost_B}\\euro $\\cdot$ {project_duration} días))")
    costs_value_content_latex.append(str(indirect_cost))
    # ------------------------------------------------------------------ #

    # === Checkpoint para ver el punto en el que se encuentra la ejecución === #
    print("\t\t\t\t» Coste indirecto del proyecto calculado")
    # ================================================================== #

    # --- Calculamos el coste total --- #
    total_cost = direct_cost + indirect_cost
    # ------------------------------------------------------------------ #

    # --- Añadimos las listas al contenido LaTex a mostrar --- #
    left_part_content_latex = " + ".join(costs_text_content_latex)
    right_part_content_latex = " + ".join(costs_value_content_latex)

    costs_content_latex = f"{left_part_content_latex} = {right_part_content_latex} = {total_cost}\\euro"
    # ------------------------------------------------------------------ #

    return total_cost, costs_content_latex