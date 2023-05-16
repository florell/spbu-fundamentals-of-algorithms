from typing import Any
import networkx as nx
from heapq import heappush, heappop
from collections import defaultdict

from src.plotting import plot_graph


def dijkstra_sp(G: nx.Graph, source_node="0") -> dict[Any, list[Any]]:
    shortest_paths = defaultdict(list)  # ключ = узел назначения, значение = список промежуточных узлов
    distances = {vertex: float("inf") for vertex in G}
    distances[source_node] = 0
    heap = [(0, source_node)]

    # Алгоритм Дейкстры на основе двоичной кучи
    while heap:
        current_distance, current_vertex = heappop(heap)

        if current_distance > distances[current_vertex]:
            continue

        # Обход соседей текущего узла для поиска минимального расстояния
        for neighbor, weight in G[current_vertex].items():
            new_distance = current_distance + weight["weight"]
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                shortest_paths[neighbor] = shortest_paths[current_vertex] + [current_vertex]
                heappush(heap, (new_distance, neighbor))

    # Построение кратчайшего пути между двумя узлами
    for vertex in G:
        shortest_paths[vertex].append(vertex)

    return shortest_paths


if __name__ == "__main__":
    G = nx.read_edgelist("practicum_3/homework/graph_1.edgelist", create_using=nx.Graph)
    plot_graph(G)
    shortest_paths = dijkstra_sp(G, source_node="0")
    test_node = "5"
    shortest_path_edges = [
        (shortest_paths[test_node][i], shortest_paths[test_node][i + 1])
        for i in range(len(shortest_paths[test_node]) - 1)
    ]
    plot_graph(G, highlighted_edges=shortest_path_edges)
