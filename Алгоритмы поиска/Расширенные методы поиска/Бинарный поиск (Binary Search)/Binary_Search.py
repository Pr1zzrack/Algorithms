def binary_search(arr, x):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Пример использования
arr = [2, 3, 4, 10, 40]
x = 10
result = binary_search(arr, x)
print("Индекс элемента", x, ":", result)


# Объяснение:

# def binary_search(arr, x):: Определение функции бинарного поиска.
# low, high = 0, len(arr) - 1: Установка начальных значений индексов нижней и верхней границ.
# while low <= high:: Использование цикла для поиска элемента.
# mid = (low + high) // 2: Находим средний индекс массива.
# if arr[mid] == x:: Проверяем, является ли средний элемент искомым.
# elif arr[mid] < x: и else:: Сужаем диапазон поиска в соответствии с результатом сравнения.
# return -1: Возвращаем -1, если элемент не найден.