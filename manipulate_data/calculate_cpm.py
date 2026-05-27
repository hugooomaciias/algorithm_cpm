import networkx as nx

from manipulate_data.calculate_earlies_lasts import calculate_earlies_function
from manipulate_data.calculate_earlies_lasts import calculate_lasts_function
from manipulate_data.calculate_slack_critical_path import calculate_slack_critical_path_function

from generate_content_latex.insert_earlies_lasts_table import insert_earlies_lasts_table_function
from generate_content_latex.insert_slack_critical_path_table import insert_slack_critical_path_table_function

def calculate_cpm_function(latex_content, tasks, graph):
    # --- Ordenamos las tareas para calcular correctamente los earlies y lasts --- #
    ordered_nodes = list(nx.topological_sort(graph))
    # ------------------------------------------------------------------ #

    # --- Definimos el early inicial --- #
    earlies = {node: 0 for node in graph.nodes()}
    # ------------------------------------------------------------------ #

    # --- Obtenemos los earlies y la duración del proyecto --- #
    earlies, project_duration, earlies_content_latex = calculate_earlies_function(tasks, graph, ordered_nodes, earlies)
    # ------------------------------------------------------------------ #

    # --- Definimos el last inicial --- #
    lasts = {node: project_duration for node in graph.nodes()}
    # ------------------------------------------------------------------ #

    # --- Obtenemos los lasts --- #
    lasts, lasts_content_latex = calculate_lasts_function(tasks, graph, ordered_nodes, lasts)
    # ------------------------------------------------------------------ #

    # === Checkpoint para ver el punto en el que se encuentra la ejecución === #
    print("\t\t\t\t» Earlies y lasts obtenidos")
    # ================================================================== #

    # --- Insertamos la tabla de earlies y lasts en el fichero LaTex --- #
    print("\t\t\t\t  📝 [LaTex] Insercción de la tabla de earlies y lasts")
    insert_earlies_lasts_table_function(latex_content, ordered_nodes, earlies_content_latex, lasts_content_latex, project_duration)
    # ------------------------------------------------------------------ #

    # --- Calculamos la holgura y el camino crítico del proyecto --- #
    critical_path, slack_content_latex, critical_path_content_latex = calculate_slack_critical_path_function(tasks, earlies, lasts)
    # ------------------------------------------------------------------ #

    # === Checkpoint para ver el punto en el que se encuentra la ejecución === #
    print("\t\t\t\t» Holgura y camino crítico calculado")
    # ================================================================== #

    # --- Insertamos la tabla de holgura --- #
    print("\t\t\t\t  📝 [LaTex] Insercción de la tabla de holgura y camino crítico")
    insert_slack_critical_path_table_function(tasks, latex_content, slack_content_latex, critical_path_content_latex, project_duration)
    # ------------------------------------------------------------------ #

    return project_duration, critical_path