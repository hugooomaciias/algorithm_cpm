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
            latex_content.append(f"\\textbf{{Iteración inicial}}")
        else:
            latex_content.append(f"\\textbf{{Iteración {iteration}}}")
        # ================================= #

        latex_content.append(r"\end{center}")
        # --------------------------------- #

        # --- Insertamos la tabla de duraciones y costes en el fichero LaTex --- #
        insert_duration_costs_table_function(latex_content, tasks)
        # --------------------------------- #

        # --- Calcular CPM inicial --- #
        project_duration, critical_path = calculate_cpm_function(latex_content, tasks, self.graph)
        # --------------------------------- #

        if (iteration == 0):
            initial_project_duration = project_duration

        # --- Construimos el diagrama de gantt --- #
        plot_data = create_gantt_chart_function(tasks, initial_project_duration)
        # --------------------------------- #

        # --- Generamos el diagrama de gantt del proyecto --- #
        generate_output_gantt_chart_function(iteration, plot_data, OUTPUT_GANTT)
        # --------------------------------- #

        # --- Insertamos el diagrama de Gantt --- #
        insert_gantt_chart_function(tasks, latex_content, initial_project_duration)
        # --------------------------------- #

        # --- Calculamos el coste total del proyecto --- #
        total_cost, costs_content_latex = calculate_total_cost_function(tasks, self.indirect_cost_A, self.indirect_cost_B, project_duration)
        # --------------------------------- #

        # --- Insertamos el coste del proyecto en LaTex --- #
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
                break
        # --------------------------------- #

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

        # --- Finalizamos la ejecución del algoritmo si no existen candidatos a reducir --- #
        if (not candidates):
            break
        # --------------------------------- #

        # --- Ordenamos los candidatos obtenidos de menor a mayor Slope --- # 
        candidates.sort(key=lambda x: tasks[x]['Slope'])
        # --------------------------------- #

        # --- Elegimos el candidato menos costoso de reducir --- #
        best_candidate = candidates[0]
        # --------------------------------- #

        # --- Aplicamos la reducción sobre el mejor candidato --- #
        tasks[best_candidate]['Current Duration'] -= 1
        tasks[best_candidate]['Current Cost'] += tasks[best_candidate]['Slope']
        # --------------------------------- #

        iteration += 1
    # ------------------------------------------------------------------ #

    # --- Redefinimos el nombre del fichero con el diagrama de Gantt óptimo --- #
    best_iter_idx, best_data = min(enumerate(history), key=lambda x: x[1]['total_cost'])

    self.optimal_duration = best_data['duration']
    self.optimal_cost = best_data['total_cost']

    if best_iter_idx == 0:
        current_output_path = "output_gantt_iter_inicial.png"
    else:
        current_output_path = f"output_gantt_iter_{best_iter_idx}.png"

    new_output_path = current_output_path.replace(".png", "_(Optimo).png")

    path_actual = os.path.join(OUTPUT_GANTT, current_output_path)
    path_nuevo = os.path.join(OUTPUT_GANTT, new_output_path)

    if os.path.exists(path_actual):
        os.rename(path_actual, path_nuevo)
    # ------------------------------------------------------------------ #

    # --- Generamos la curva de Coste / Tiempo del proyecto --- #
    generate_output_cost_time_curve_function(history, OUTPUT_COST_TIME_CURVE)
    # ------------------------------------------------------------------ #

    # --- Insertamos el diagrama de Gantt --- #
    insert_cost_time_curve_function(latex_content, history)
    # ------------------------------------------------------------------ #

    # --- Insertamos la ultima linea en latex que cierra el documento --- #
    latex_content.append(r"\end{document}")
    # ------------------------------------------------------------------ #