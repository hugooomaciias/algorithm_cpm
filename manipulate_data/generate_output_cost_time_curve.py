import matplotlib.pyplot as plt

def generate_output_cost_time_curve_function(history, OUTPUT_COST_TIME_CURVE):
    # --- Obtenemos las duraciones y costes para representarlas en el gráfico --- #
    durations = [iter['duration'] for iter in history]
    costs = [iter['total_cost'] for iter in history]
    # ------------------------------------------------------------------ #

    # === Checkpoint para ver el punto en el que se encuentra la ejecución === #
    print("\t\t\t» Duraciones y costes obtenidos para cada iteración")
    # ================================================================== #

    # --- Establecemos el tamaño de la imagen --- #
    plt.figure(figsize=(8, 5))
    # ------------------------------------------------------------------ #
    
    # --- Dibujamos la línea y los marcadores del gráfico --- #
    plt.plot(durations, costs, marker='o', linestyle='-', color='#a3b18a', markerfacecolor='#344e41', markeredgecolor='#344e41', linewidth=2, label='Coste Total Proyecto')
    # ------------------------------------------------------------------ #

    # --- Encontramos y marcamos punto óptimo donde la duración y el coste son mínimos --- #
    min_cost = min(costs)
    min_index = costs.index(min_cost)
    optimal_duration = durations[min_index]

    plt.scatter(optimal_duration, min_cost, color='#344e41', s=100, zorder=5, label=f'Óptimo ({int(min_cost)}€)')
    # ------------------------------------------------------------------ #

    # --- Añadimos una anotación en el punto óptimo para informarción --- #
    plt.annotate('Duración\nóptima', 
                 xy=(optimal_duration, min_cost), 
                 xytext=(0, 30),
                 textcoords='offset points',
                 arrowprops=dict(facecolor='black', shrink=0.1, width=0.8, headwidth=7),
                 horizontalalignment='center')
    # ------------------------------------------------------------------ #

    # === Checkpoint para ver el punto en el que se encuentra la ejecución === #
    print("\t\t\t» Gráfico con los datos de cada iteración marcados creado")
    # ================================================================== #

    # --- Establecemos los títulos de cada eje y del propio diagrama --- #
    plt.title("Curva de Coste / Tiempo (Crashing)", fontsize=14, fontweight='bold', pad=15)
    plt.xlabel("Duración del Proyecto (Días)", fontsize=14, labelpad=15)
    plt.ylabel("Coste Total (€)", fontsize=14, labelpad=15)
    # ------------------------------------------------------------------ #

    # --- Coonfiguramos el grid e insertamos la leyenda --- #
    plt.grid(True, linestyle='--', alpha=0.3)
    plt.legend()
    # ------------------------------------------------------------------ #

    # --- Ivertimos el eje X para mostrar la mayor duración a la izquierda del gráfico --- #
    plt.gca().invert_xaxis()
    # ------------------------------------------------------------------ #

    # === Checkpoint para ver el punto en el que se encuentra la ejecución === #
    print("\t\t\t» Configuración final establecida")
    # ================================================================== #

    # --- Guardamos la imagen en el fichero de salida y cerramos el gráfico --- #
    plt.tight_layout()
    plt.savefig(OUTPUT_COST_TIME_CURVE, dpi=300)
    plt.close()
    # ------------------------------------------------------------------ #