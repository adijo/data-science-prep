from typing import List, Set, Dict


class Graph:
    _graph: Dict[int, Set[int]] = dict()

    def _has_node(self, idx: int) -> bool:
        return idx in self._graph

    def add_edge(self, one: int, two: int) -> None:
        if one not in self._graph:
            self._graph[one] = set()
        if two not in self._graph:
            self._graph[two] = set()

        self._graph[one].add(two)
        self._graph[two].add(one)

    def get_neighbours(self, idx: int) -> Set[int]:
        assert self._has_node(idx)
        return self._graph.get(idx)


def make_graph(adjacency_matrix: List[List[int]]) -> Graph:
    graph: Graph = Graph()
    for i in range(len(adjacency_matrix)):
        for j in range(len(adjacency_matrix[0])):
            if adjacency_matrix[i][j] == 1:
                graph.add_edge(i, j)
    return graph


def topic_groups(adjacency_matrix: List[List[int]]) -> int:
    graph: Graph = make_graph(adjacency_matrix)
    topics: int = 0
    visited: Set[int] = set()
    for node in range(len(adjacency_matrix)):
        if node not in visited:
            topics += 1
            visit(node, graph, visited)
    return topics


def visit(node: int, graph: Graph, visited: Set[int]) -> None:
    for neighbour in graph.get_neighbours(node):
        if neighbour not in visited:
            visited.add(neighbour)
            visit(neighbour, graph, visited)


assert (
    topic_groups([[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 1]])
    == 3
)

assert (
    topic_groups([[1, 1, 1, 1, 0], [1, 1, 0, 1, 0], [1, 1, 0, 0, 0], [0, 0, 0, 0, 0]])
    == 1
)
