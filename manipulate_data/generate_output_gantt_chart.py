import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.ticker as ticker

def generate_output_gantt_chart_function(iteration, plot_data, OUTPUT_GANTT):
    # --- Obtenemos el número de tareas existentes y sus respectivos nombres --- #
    labels = [d['label'] for d in plot_data]
    y_positions = range(len(labels))
    max_duration = plot_data[0]['project_duration']
    # ------------------------------------------------------------------ #

    # --- Configuramos la altura del diagrama en base al numero de tareas --- #
    _, ax = plt.subplots(figsize=(12, max(5, len(labels) * 0.6)))
    # ------------------------------------------------------------------ #

    # === Checkpoint para ver el punto en el que se encuentra la ejecución === #
    print("\t\t\t\t» Configuración inicial establecida")
    # ================================================================== #

    # --- Dibujamos las barras de duración para cada tarea en el diagrama --- #
    non_critical_reduced = False

    for i, task in enumerate(plot_data):
        # --- Establecemos el color de la barra en función de si es crítica o no --- #
        if (task['critical'] == "Sí"):
            color = '#ff6b6b'
            edge_color = '#841818'
        else:
            color = '#a3b18a'
            edge_color = '#344e41'
        # --------------------------------- #
        
        # --- Creamos la barra --- #
        ax.barh(i, task['normal_duration'], left=task['start'], height=0.5, 
                color=color, edgecolor=edge_color, alpha=0.5, linewidth=2)
        ax.barh(i, task['current_duration'], left=task['start'], height=0.5, 
                color=color, edgecolor=edge_color, linewidth=2)
        
        if ((task['normal_duration'] != task['current_duration']) and (task['critical'] == "No")):
            non_critical_reduced = True
        # --------------------------------- #
        
        # --- Creamos la barra de holgura si es que la tarea tiene --- #
        if ((task['slack'] > 0) and (not non_critical_reduced)):
            # --- Creamos la barra --- #
            ax.barh(i, task['slack'], left=task['start'] + task['current_duration'], height=0.3,
                    color='gray', alpha=0.3, hatch='///', edgecolor='gray', linewidth=1.5)
            # --------------------------------- #
            
            # --- Indicamos la holgura que la tarea posee --- #
            ax.text(task['start'] + task['current_duration'] + task['slack'] + 0.1, i, 
                    f"+{int(task['slack'])}", va='center', fontsize=8, color='gray')
            # --------------------------------- #
        # --------------------------------- #

        # --- Mostramos el nombre de la tarea en la propia barra --- #
        ax.text(task['start'] + task['normal_duration'] - 0.2, i, task['label'], 
                va='center', ha='center', color=edge_color, fontweight='bold')
        # --------------------------------- #
    # ------------------------------------------------------------------ #

    # === Checkpoint para ver el punto en el que se encuentra la ejecución === #
    print("\t\t\t\t» Barras para cada tarea creadas")
    # ================================================================== #

    # --- Configuramos diferentes aspectos del diagrama --- #
    # --- Ivertimos el eje Y para mostrar la primera tarea arriba del diagrama --- #    
    ax.invert_yaxis()
    # --------------------------------- #
    
    # --- Establecemos los títulos de cada eje y del propio diagrama --- #
    ax.set_xlabel("Tiempo (días)", fontsize=14, labelpad=15)
    ax.set_ylabel("Tareas", fontsize=14, labelpad=15)
    ax.set_title("Diagrama de Gantt", fontsize=14, pad=15, fontweight='bold')
    # --------------------------------- #
        
    # --- Configuramos el eje X --- #
    ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
    ax.grid(True, axis='x', linestyle='--', alpha=0.3)
    ax.set_xlim(0, max_duration)
    # --------------------------------- #
        
    # --- Configuramos el eje X --- #
    ax.set_yticks(y_positions)
    ax.set_yticklabels(labels)
    # --------------------------------- #

    # --- Insertamos la leyenda arriba a la derecha --- #
    handles = [
        mpatches.Patch(color='#a3b18a', label='Tarea no crítica (Plan. Extrema)'),
        mpatches.Patch(color='#ff6b6b', label='Tarea crítica (Plan. Extrema)'),
        mpatches.Patch(color='#ff6b6b', alpha=0.5, label='Tarea crítica (Plan. Normal)'),
        mpatches.Patch(facecolor='gray', alpha=0.3, hatch='///', label='Holgura')
    ]

    ax.legend(handles=handles, loc='upper right')
    # --------------------------------- #
    # ------------------------------------------------------------------ #

    # === Checkpoint para ver el punto en el que se encuentra la ejecución === #
    print("\t\t\t\t» Configuración final establecida")
    # ================================================================== #

    # --- Obtenemos la ruta del fichero de salida --- #
    output_path = ""
    
    if (iteration == 0):
        output_path = f"{OUTPUT_GANTT}output_gantt_iter_inicial.png"
    else:
        output_path = f"{OUTPUT_GANTT}output_gantt_iter_{iteration}.png"

    # --- Guardamos la imagen en el fichero de salida y cerramos el diagrama --- #
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    # ------------------------------------------------------------------ #