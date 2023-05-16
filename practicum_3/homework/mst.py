from typing import Any

import matplotlib.pyplot as plt
import networkx as nx

from src.plotting import plot_graph


def prim_mst(G: nx.Graph, start_node="0") -> set[tuple[Any, Any]]:
    mst_set = set()  # множество узлов, включенных в остовное дерево (MST)
    rest_set = set(G.nodes())  # множество узлов, еще не включенных в MST
    mst_edges = set()  # множество ребер, составляющих MST

    # Начинаем с указанного start_node
    current_node = start_node
    mst_set.add(current_node)
    rest_set.remove(current_node)

    # Повторяем, пока все узлы не будут включены в MST
    while rest_set:
        min_weight = float('inf')
        min_edge = None

        # Находим ребро минимального веса, соединяющее current_node с любым узлом из rest_set
        for node in mst_set:
            for neighbor, weight in G[node].items():
                print(weight['weight'], min_weight)
                if neighbor in rest_set and weight['weight'] < min_weight:
                    min_weight = weight['weight']
                    min_edge = (node, neighbor)

        # Добавляем ребро минимального веса в MST
        mst_edges.add(min_edge)
        mst_set.add(min_edge[1])
        rest_set.remove(min_edge[1])

    return mst_edges


if __name__ == "__main__":
    G = nx.read_edgelist("practicum_3/homework/graph_1.edgelist", create_using=nx.Graph)
    plot_graph(G)
    mst_edges = prim_mst(G, start_node="0")
    plot_graph(G, highlighted_edges=list(mst_edges))
