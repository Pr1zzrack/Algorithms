def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

# Пример использования
arr = [64, 34, 25, 12, 22, 11, 90]
arr = quick_sort(arr)
print("Отсортированный массив:", arr)


# Объяснение:

# def quick_sort(arr):: Объявление функции быстрой сортировки.
# if len(arr) <= 1:: Базовый случай, возвращаем массив, если он состоит из одного элемента или пуст.
# pivot = arr[0]: Выбор опорного элемента (в данном случае, первого элемента).
# less = [x for x in arr[1:] if x <= pivot]: Создание списка элементов меньших или равных опорному.
# greater = [x for x in arr[1:] if x > pivot]: Создание списка элементов больших опорного.
# return quick_sort(less) + [pivot] + quick_sort(greater): Рекурсивное объединение отсортированных подмассивов и опорного элемента.