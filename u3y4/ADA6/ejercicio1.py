import networkx as nx
import matplotlib.pyplot as plt

def solicitar_datos():
    estados = []
    while len(estados) < 7:
        estado = input(f"Ingrese el nombre del estado {len(estados) + 1}: ")
        estados.append(estado)
    
    costos = {}
    for origen in estados:
        for destino in estados:
            if origen != destino:
                costo = int(input(f"Ingrese el costo de traslado de {origen} a {destino}: "))
                costos[(origen, destino)] = costo
    
    return estados, costos

def calcular_costo_total(recorrido, costos):
    costo_total = 0
    for i in range(len(recorrido) - 1):
        origen = recorrido[i]
        destino = recorrido[i + 1]
        costo_total += costos[(origen, destino)]
    return costo_total

def dibujar_grafo(G, costos):
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=1500, node_color="skyblue", font_size=10, font_weight="bold", edge_color="gray")
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()

print("Por favor ingrese los datos:")
estados, costos = solicitar_datos()

G = nx.Graph()

G.add_nodes_from(estados)

for origen, destino in costos.keys():
    peso = costos[(origen, destino)]
    G.add_edge(origen, destino, weight=peso)

print("\nGrafo generado:")
dibujar_grafo(G, costos)

recorrido_sin_repetir = list(nx.dfs_preorder_nodes(G, source=estados[0]))
costo_total_sin_repetir = calcular_costo_total(recorrido_sin_repetir, costos)

recorrido_con_repetidos = list(nx.dfs_postorder_nodes(G, source=estados[0]))
costo_total_con_repetidos = calcular_costo_total(recorrido_con_repetidos, costos)

print("\nRecorrido sin repetir estados:", ' -> '.join(recorrido_sin_repetir))
print("Costo total (sin repetir estados):", costo_total_sin_repetir)
print("\nRecorrido permitiendo repetir estados:", ' -> '.join(recorrido_con_repetidos))
print("Costo total (permitiendo repetir estados):", costo_total_con_repetidos)