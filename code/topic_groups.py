from collections import defaultdict
from typing import List, Set, DefaultDict


class Graph:
    _graph: DefaultDict[int, Set[int]] = defaultdict(set)

    def add_edge(self, one: int, two: int) -> None:
        self._graph[one].add(two)
        self._graph[two].add(one)

    def get_neighbours(self, idx: int) -> Set[int]:
        return self._graph.get(idx)


def make_graph(adjacency_matrix: List[List[int]]) -> Graph:
    graph = Graph()
    for i in range(len(adjacency_matrix)):
        for j in range(len(adjacency_matrix[0])):
            if adjacency_matrix[i][j] == 1:
                graph.add_edge(i, j)
    return graph


def topic_groups(adjacency_matrix: List[List[int]]) -> int:
    num_nodes: int = len(adjacency_matrix)
    graph: Graph = make_graph(adjacency_matrix)
    topics: int = 0
    visited: Set[int] = set()

    def visit(curr_node: int) -> None:
        for neighbour in graph.get_neighbours(curr_node):
            if neighbour not in visited:
                visited.add(neighbour)
                visit(neighbour)

    for node in range(num_nodes):
        if node not in visited:
            visit(node)
            topics += 1

    return topics





assert (
    topic_groups([[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 1]])
    == 3
)

assert (
    topic_groups([[1, 1, 1, 1, 0], [1, 1, 0, 1, 0], [1, 1, 0, 0, 0], [0, 0, 0, 0, 0]])
    == 1
)
