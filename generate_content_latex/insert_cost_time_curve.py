def insert_cost_time_curve_function(latex_content, history):
    # --- Inicializamos las variables necesarias --- #
    coordinates = ""
    # ------------------------------------------------------------------ #
    
    # --- Añidamos todas las coordenadas y buscamos el punto óptimo --- #
    min_cost = float('inf')
    optimal_duration = 0

    for iter in history:
        # --- Obtenemos la duración y el coste para cada iteración --- #
        duration = iter['duration']
        cost = iter['total_cost']
        # --------------------------------- #
        
        # --- Añadimos la duración y el coste de la iteración a las coordenadas --- #
        coordinates += f"({duration},{cost}) "
        # --------------------------------- #

        # --- Obtenemos el punto óptimo --- #
        if (cost < min_cost):
            min_cost = cost
            optimal_duration = duration
        # --------------------------------- #
    # ------------------------------------------------------------------ #

    # --- Ponemos el título de la sección, abrimos la figura y el gráfico indicando sus opciones --- #
    latex_content.append(r"")
    latex_content.append(r"\newpage")
    latex_content.append(r"")
    latex_content.append(r"\textbf{Curva Coste / Tiempo}")
    latex_content.append(r"\begin{figure}")
    latex_content.append(r"\centering")
    latex_content.append(r"\begin{tikzpicture}")
    latex_content.append(r"\begin{axis}[title={\textbf{Curva Coste / Tiempo}}, xlabel={Duración (días)}, ylabel={Coste Total (\euro)}, width=10cm, height=7cm, grid=major, grid style={dashed,gray!30}, x dir=reverse]")
    # ------------------------------------------------------------------ #
    
    # --- Dibujamos la línea del gráfico y marcamos los puntos de las diferentes iteraciones --- #
    latex_content.append(fr"\addplot[color={{Normal}}, mark=*, thick, mark options={{fill={{EdgeNormal}}, draw={{EdgeNormal}}, solid}}] coordinates {{{coordinates}}};")
    # ------------------------------------------------------------------ #
    
    # --- Añadimos la leyenda --- #
    latex_content.append(r"\addlegendentry{Coste Total}")
    # ------------------------------------------------------------------ #

    # --- Añadimos una anotación en el punto óptimo para informarción --- #
    label_optimo = r"Duración \\ óptima"
    latex_content.append(fr"\node[coordinate, pin={{[align=center]90:{{{label_optimo}}}}}] at (axis cs:{optimal_duration},{min_cost}) {{}};")
    # ------------------------------------------------------------------ #

    # --- Cerramos el gráfico y la figura --- #
    latex_content.append(r"\end{axis}")
    latex_content.append(r"\end{tikzpicture}")
    latex_content.append(r"\end{figure}")
    # ------------------------------------------------------------------ #