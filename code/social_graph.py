from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from typing import List, Dict, Tuple

NO_FRIENDSHIP = -1


@dataclass
class User:
    user_id: str
    friends: List[User]

    def __eq__(self: User, other: User) -> bool:
        return self.user_id == other.user_id

    def __hash__(self: User) -> int:
        return hash(self.user_id)

    def __str__(self: User) -> str:
        return self.user_id


def make_friendship_graph(
    nodes: List[str], edges: List[Tuple[str, str]]
) -> Dict[str, User]:
    """
    We assume that the graph is connected for this example.
    """

    user_graph: Dict[str, User] = {
        node: User(user_id=node, friends=list()) for node in nodes
    }

    for edge in edges:
        node_a, node_b = edge
        user_graph[node_a].friends.append(user_graph[node_b])
        user_graph[node_b].friends.append(user_graph[node_a])

    return user_graph


def smallest_friendships(from_user: User, to_user: User) -> int:
    q = deque([(from_user, 0)])
    visited = {from_user}

    while len(q) > 0:
        top, dist = q.popleft()

        if top == to_user:
            return dist - 1

        for friend in top.friends:
            if friend not in visited:
                visited.add(friend)
                q.append((friend, dist + 1))

    return NO_FRIENDSHIP


graph = make_friendship_graph(
    nodes=["a", "b", "c", "d", "e"],
    edges=[("a", "b"), ("b", "d"), ("a", "c"), ("b", "d"), ("d", "e")],
)
assert smallest_friendships(graph["a"], graph["e"]) == 2
assert smallest_friendships(graph["a"], graph["c"]) == 0
assert smallest_friendships(graph["c"], graph["e"]) == 3
