class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# Пример использования
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)


# Объяснение:

# class TreeNode:: Определение класса узла дерева.
# def __init__(self, key):: Конструктор класса, инициализирующий узел с данными key и указателями на левого и правого потомков.
# self.left = None: Инициализация указателя на левого потомка.
# self.right = None: Инициализация указателя на правого потомка.
# self.val = key: Присвоение значения узлу.
# Создание объекта дерева с корневым узлом, левым и правым потомками.