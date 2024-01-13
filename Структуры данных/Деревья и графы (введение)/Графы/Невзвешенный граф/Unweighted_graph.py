class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, start, end):
        if start in self.graph:
            self.graph[start].append(end)
        else:
            self.graph[start] = [end]

# Пример использования
graph = Graph()
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 3)
graph.add_edge(3, 1)