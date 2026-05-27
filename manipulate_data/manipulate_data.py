import os

from manipulate_data.calculate_cpm import calculate_cpm_function
from manipulate_data.calculate_total_cost import calculate_total_cost_function
from manipulate_data.create_gantt_chart import create_gantt_chart_function
from manipulate_data.generate_output_gantt_chart import generate_output_gantt_chart_function
from manipulate_data.generate_output_cost_time_curve import generate_output_cost_time_curve_function

from generate_content_latex.insert_gantt_chart import insert_gantt_chart_function
from generate_content_latex.insert_duration_costs_table import insert_duration_costs_table_function
from generate_content_latex.insert_project_cost import insert_project_cost_function
from generate_content_latex.insert_cost_time_curve import insert_cost_time_curve_function

def manipulate_data_function(self, OUTPUT_GANTT, OUTPUT_COST_TIME_CURVE):
    os.makedirs(OUTPUT_GANTT, exist_ok=True)

    # --- Definimos las variables necesarias  --- #
    history = []
    iteration = 0
    initial_project_duration = 0

    tasks = self.tasks
    latex_content = self.latex_content
    # ------------------------------------------------------------------ #

    # --- Iteremos los diferentes estados de la manipulación de datos para crear la curva Coste/Tiempo --- #
    while True:
        # --- Insertamos la apertura de la iteración --- #
        latex_content.append(r"")
        latex_content.append(r"\newpage")
        latex_content.append(r"")
        latex_content.append(r"\begin{center}")

        # === Checkpoint para ver la iteración en la que se encuentra la ejecución === #
        if (iteration == 0):
            print("\t\t➤  Iteración inicial")

            latex_content.append(f"\\textbf{{Iteración inicial}}")
        else:
            print(f"\n\t\t➤  Iteración {iteration}")

            latex_content.append(f"\\textbf{{Iteración {iteration}}}")
        # ================================= #

        latex_content.append(r"\end{center}")
        # --------------------------------- #

        # --- Insertamos la tabla de duraciones y costes en el fichero LaTex --- #
        print("\t\t  📝 [LaTex] Insercción de la tabla de duraciones y costes")
        insert_duration_costs_table_function(latex_content, tasks)
        # --------------------------------- #

        # === Checkpoint para ver la fase en la que se encuentra la ejecución === #
        print("\n\t\t\t[1] Cálculo del CPM")
        # ================================= #

        # --- Calcular CPM inicial --- #
        project_duration, critical_path = calculate_cpm_function(latex_content, tasks, self.graph)
        # --------------------------------- #

        # === Checkpoint para ver la fase en la que se encuentra la ejecución === #
        print("\n\t\t\t[2] Creación del diagrama de Gantt")
        # ================================= #

        if (iteration == 0):
            initial_project_duration = project_duration

        # --- Construimos el diagrama de gantt --- #
        plot_data = create_gantt_chart_function(tasks, initial_project_duration)
        # --------------------------------- #

        # === Checkpoint para ver el punto en el que se encuentra la ejecución === #
        print("\t\t\t\t» Instantes de tiempo de inicio y fin obtenidos para cada tarea")
        # ================================================================== #

        # --- Generamos el diagrama de gantt del proyecto --- #
        generate_output_gantt_chart_function(iteration, plot_data, OUTPUT_GANTT)
        # --------------------------------- #

        # === Checkpoint para ver el punto en el que se encuentra la ejecución === #
        print("\t\t\t\t» Fichero de salida para el diagrama de Gantt generado ✔")
        # ================================= #

        # --- Insertamos el diagrama de Gantt --- #
        print("\t\t\t\t  📝 [LaTex] Insercción del diagrama de Gantt")
        insert_gantt_chart_function(tasks, latex_content, initial_project_duration)
        # --------------------------------- #

        # === Checkpoint para ver la fase en la que se encuentra la ejecución === #
        print("\n\t\t\t[3] Cálculo del coste del proyecto")
        # ================================= #

        # --- Calculamos el coste total del proyecto --- #
        total_cost, costs_content_latex = calculate_total_cost_function(tasks, self.indirect_cost_A, self.indirect_cost_B, project_duration)
        # --------------------------------- #

        # === Checkpoint para ver el punto en el que se encuentra la ejecución === #
        print("\t\t\t\t» Coste total del proyecto calculado")
        # ================================= #

        # --- Insertamos el coste del proyecto en LaTex --- #
        print("\t\t\t\t  📝 [LaTex] Insercción del coste del proyecto")
        insert_project_cost_function(latex_content, costs_content_latex)
        # --------------------------------- #

        # --- Guardamos el estado del algoritmo para generar la gráfica --- #
        history.append({
            'duration': project_duration,
            'total_cost': total_cost
        })
        # --------------------------------- #

        # --- Paramos la ejecución si el coste ha subido en las 2 últimas iteraciones consecutivas --- #
        if (len(history) >= 3):
            actual_cost = history[-1]['total_cost']
            previous_cost = history[-2]['total_cost']
            previous_previous_cost = history[-3]['total_cost']

            # Si el coste actual es mayor que el anterior Y el anterior mayor que el de hace 2
            if ((actual_cost > previous_cost) and (previous_cost > previous_previous_cost)):
                # === Indicación de finalización del algoritmo === #
                print("\n\t\tℹ Deteniendo algoritmo: El coste ha aumentado en las dos últimas iteraciones consecutivas")
                # ================================= #

                break
        # --------------------------------- #

        # === Checkpoint para ver la fase en la que se encuentra la ejecución === #
        print("\n\t\t\t[4] Reducción de las duraciones")
        # ================================= #

        # --- Obtenemos los nuevos candidatos a reducir --- #
        candidates = []

        for task in critical_path:
            current_duration = tasks[task]['Current Duration']
            crash_duration = tasks[task]['Crash Duration']
            current_cost = tasks[task]['Current Cost']
            crash_cost = tasks[task]['Crash Cost']

            if ((current_duration > crash_duration) and (current_cost < crash_cost)):
                candidates.append(task)
        # --------------------------------- #
        
        # === Checkpoint para ver el punto en el que se encuentra la ejecución === #
        print("\t\t\t\t» Nuevos candidatos a reducir obtenidos")
        # ================================= #

        # --- Finalizamos la ejecución del algoritmo si no existen candidatos a reducir --- #
        if (not candidates):
            # === Indicación de finalización del algoritmo === #
            print("\n\t\tℹ Deteniendo algoritmo: Limite de reducción máxima alcanzado porque no existen más candidatos")
            # ================================= #
            
            break
        # --------------------------------- #

        # --- Ordenamos los candidatos obtenidos de menor a mayor Slope --- # 
        candidates.sort(key=lambda x: tasks[x]['Slope'])
        # --------------------------------- #

        # --- Elegimos el candidato menos costoso de reducir --- #
        best_candidate = candidates[0]
        # --------------------------------- #

        # === Checkpoint para ver el punto en el que se encuentra la ejecución === #
        print("\t\t\t\t» Mejor candidato elegido")
        # ================================= #

        # --- Aplicamos la reducción sobre el mejor candidato --- #
        tasks[best_candidate]['Current Duration'] -= 1
        tasks[best_candidate]['Current Cost'] += tasks[best_candidate]['Slope']
        # --------------------------------- #

        # === Checkpoint para ver el punto en el que se encuentra la ejecución === #
        print("\t\t\t\t» Reducción aplicada al mejor candidato")
        # ================================= #

        iteration += 1
    # ------------------------------------------------------------------ #

    # --- Redefinimos el nombre del fichero con el diagrama de Gantt óptimo --- #
    best_iter_idx, _ = min(enumerate(history), key=lambda x: x[1]['total_cost'])

    if best_iter_idx == 0:
        current_output_path = "output_gantt_iter_inicial.png"
    else:
        current_output_path = f"output_gantt_iter_{best_iter_idx}.png"

    new_output_path = current_output_path.replace(".png", "_(Optimo).png")

    path_actual = os.path.join(OUTPUT_GANTT, current_output_path)
    path_nuevo = os.path.join(OUTPUT_GANTT, new_output_path)

    os.rename(path_actual, path_nuevo)
    # ------------------------------------------------------------------ #

    # === Checkpoint para ver la fase en la que se encuentra la ejecución === #
    print("\n\t\t[5] Creación de la curva Coste / Tiempo")
    # ================================================================== #

    # --- Generamos la curva de Coste / Tiempo del proyecto --- #
    generate_output_cost_time_curve_function(history, OUTPUT_COST_TIME_CURVE)
    # ------------------------------------------------------------------ #

    # === Checkpoint para ver el punto en el que se encuentra la ejecución === #
    print("\t\t\t» Fichero de salida para la curva de Coste / Tiempo generado ✔")
    # ================================================================== #

    # --- Insertamos el diagrama de Gantt --- #
    print("\t\t\t  📝 [LaTex] Insercción de la curva Coste / Tiempo")
    insert_cost_time_curve_function(latex_content, history)
    # ------------------------------------------------------------------ #

    # --- Insertamos la ultima linea en latex que cierra el documento --- #
    latex_content.append(r"\end{document}")
    # ------------------------------------------------------------------ #