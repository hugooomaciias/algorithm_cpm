import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

from upload_definition_data.generate_layers import generate_layers_function
from upload_definition_data.generate_layers import sort_key_function

def generate_output_graph_function(tasks, graph, OUTPUT_GRAPH):
    # --- Establecemos el tamaño de la imagen --- #
    plt.figure(figsize=(8, 5))
    # ------------------------------------------------------------------ #

    # --- Establecemos el layout del grafo --- #
    # --- Obtenmos las columnas --- #
    layers = generate_layers_function(tasks)
    # --------------------------------- #

    # --- Creamos y definimos las variables necesarias --- #
    pos = {}
    x_sep = 3.0
    y_sep = 2.0
    # --------------------------------- #

    # --- Construimos las posiciones del grafo mediante las diferentes columnas --- #
    for i, nodes in enumerate(layers):
        # --- Calculamos la posición horizontal de esta columna --- #
        x = i * x_sep
        # --------------------------------- #
        
        if (i > 0):
            # --- Resto de columnas excepto la primera --- #
            # --- Creamos un subrgafo por caa columna, y añadimos sus nodos correspondientes --- #
            subgraph = nx.DiGraph()
            subgraph.add_nodes_from(nodes)
            # --------------------------------- #
            
            # --- Añadimos las aristas de este subgrafo --- #
            for start_node in nodes:
                for end_node in nodes:
                    if ((start_node != end_node) and (graph.has_edge(start_node, end_node))):
                        subgraph.add_edge(start_node, end_node)
            # --------------------------------- #

            # --- Definimos la posición de los nodos en los que haya conflicto --- #
            nodes_sorted = list(nx.lexicographical_topological_sort(
                subgraph, 
                key=lambda n: sort_key_function(n, graph, pos)
            ))

            nodes[:] = nodes_sorted
            # --------------------------------- #
            # --------------------------------- #
        else:
            # --- Primera columna --- #
            nodes.sort()
            # --------------------------------- #

        # --- Asignación de Coordenadas (X, Y) ---
        # Centramos la columna verticalmente:
        # Calculamos la altura total de esta columna para centrarla en Y=0
        col_height = (len(nodes) - 1) * y_sep
        start_y = col_height / 2
        
        for j, node in enumerate(nodes):
            y = start_y - (j * y_sep)
            pos[node] = (x, y) 
    # --------------------------------- #
    # ------------------------------------------------------------------ #

    # --- Dibujamos los nodos del grafo --- #
    nx.draw_networkx_nodes(graph, pos, node_size=700, node_color='#a3b18a', edgecolors='#344e41', linewidths=1.5)
    # ------------------------------------------------------------------ #
    
    # --- Dibujamos las etiquetas de los nodos del grafo --- #
    nx.draw_networkx_labels(graph, pos, font_size=12, font_weight='bold', font_color='#344e41')
    # ------------------------------------------------------------------ #

    # --- Creamos las aristas que unen cada nodo --- #
    solid_edges = [e for e in graph.edges() if graph[e[0]][e[1]].get('style') != 'dashed']
    dashed_edges = [e for e in graph.edges() if graph[e[0]][e[1]].get('style') == 'dashed']
    # ------------------------------------------------------------------ #

    # --- Dibujamos las aristas que unen cada nodo --- #
    nx.draw_networkx_edges(graph, pos, edgelist=solid_edges, edge_color='#293831', node_size=700, arrows=True, arrowstyle='->', arrowsize=15)
    nx.draw_networkx_edges(graph, pos, edgelist=dashed_edges, edge_color='#293831', alpha=0.5, style='dashed', node_size=700, arrows=True, arrowstyle='->', arrowsize=15)
    # ------------------------------------------------------------------ #

    # --- Dibujamos las etiquetas de los aristas que unen cada nodo del grafo --- #
    edge_labels = nx.get_edge_attributes(graph, 'label')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_size=10, font_color='#293831', font_weight='bold')
    # ------------------------------------------------------------------ #

    # --- Guardamos la imagen en el fichero de salida y cerramos el grafo --- #
    plt.title("Grafo CPM", fontsize=14, fontweight='bold')
    plt.axis('off')
    plt.savefig(OUTPUT_GRAPH, format="PNG", dpi=300)
    plt.close()
    # ------------------------------------------------------------------ #