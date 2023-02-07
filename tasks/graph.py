from typing import Any

__all__ = (
    'Node',
    'Graph'
)


class Node:
    def __init__(self, value: Any):
        self.value = value

        self.outbound = []
        self.inbound = []

    def point_to(self, other: 'Node'):
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self):
        return f'Node({repr(self.value)})'

    __repr__ = __str__


class Graph:
    def __init__(self, root: Node):
        self._root = root

    def dfs(self) -> list[Node]:
        visited = [self._root]
        queue = self._root.outbound
        while queue:
            node = queue[0]
            if node not in visited:
                visited.append(node)
            queue.pop(0)
            [queue.insert(0, neighbor) for neighbor in node.outbound[::-1] if neighbor not in visited]
        return visited

    def bfs(self) -> list[Node]:
        result_list = []
        graph_level = [self._root]
        while graph_level:
            [result_list.append(node) for node in graph_level if node not in result_list]
            queue = []
            for neighbor in graph_level:
                [queue.append(neighbor) for neighbor in neighbor.outbound if neighbor not in result_list]
            graph_level = queue
        return result_list
