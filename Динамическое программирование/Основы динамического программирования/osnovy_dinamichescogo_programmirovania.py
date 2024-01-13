def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]

# Пример использования
result = fib(5)
print("Пятый элемент последовательности Фибоначчи:", result)


# Объяснение:

# def fib(n, memo={}):: Определение функции для вычисления n-го числа Фибоначчи с использованием мемоизации.
# if n in memo:: Проверка, было ли уже вычислено значение для n.
# return memo[n]: Возвращение сохраненного значения, если оно уже было вычислено.
# if n <= 2:: Базовый случай: первые два числа Фибоначчи равны 1.
# memo[n] = fib(n-1, memo) + fib(n-2, memo): Рекурсивное вычисление значения для n и сохранение его в мемо.
# return memo[n]: Возвращение вычисленного значения.