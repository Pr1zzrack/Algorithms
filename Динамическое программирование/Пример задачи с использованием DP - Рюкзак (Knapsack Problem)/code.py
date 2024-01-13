def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]

# Пример использования
weights = [1, 2, 3]
values = [6, 10, 12]
capacity = 5
result = knapsack(weights, values, capacity)
print("Максимальная стоимость рюкзака:", result)


# Объяснение:

# def knapsack(weights, values, capacity):: Определение функции для решения задачи о рюкзаке.
# n = len(weights): Получение количества предметов.
# dp = [[0] * (capacity + 1) for _ in range(n + 1)]: Инициализация двумерного массива для хранения результатов подзадач.
# Динамическое программирование с использованием двумерного массива для хранения оптимальных решений подзадач.
# return dp[n][capacity]: Возвращение значения для задачи о рюкзаке с использованием динамического программирования.