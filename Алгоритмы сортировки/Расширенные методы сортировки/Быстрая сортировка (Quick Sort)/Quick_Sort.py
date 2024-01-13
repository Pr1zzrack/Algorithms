def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Пример использования
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = quick_sort(arr)
print("Отсортированный массив:", sorted_arr)


# Объяснение:

# def quick_sort(arr):: Определение функции быстрой сортировки.
# if len(arr) <= 1:: Проверка, нужно ли сортировать массив. Если длина массива 1 или менее, он уже отсортирован.
# pivot = arr[len(arr) // 2]: Выбор опорного элемента (pivot).
# left = [x for x in arr if x < pivot], middle = [x for x in arr if x == pivot], и right = [x for x in arr if x > pivot]: Разделение массива на три части - меньшие, равные и большие опорного элемента.
# return quick_sort(left) + middle + quick_sort(right): Рекурсивное применение быстрой сортировки к меньшим и большим частям, а затем объединение их с частью, равной опорному элементу.