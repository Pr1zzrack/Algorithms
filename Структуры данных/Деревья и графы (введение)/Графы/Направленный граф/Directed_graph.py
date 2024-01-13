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


# Объяснение:

# class Graph:: Определение класса графа.
# def __init__(self):: Конструктор класса, создающий пустой граф.
# self.graph = {}: Инициализация словаря для хранения списка смежности.
# def add_edge(self, start, end):: Метод для добавления направленного ребра в граф.
# if start in self.graph:: Проверка, существует ли уже вершина start в графе.
# self.graph[start].append(end): Добавление вершины end в список смежности вершины start.
# else:: Если вершина start не существует, создается новая запись в словаре.
# self.graph[start] = [end]: Создание новой записи в словаре.