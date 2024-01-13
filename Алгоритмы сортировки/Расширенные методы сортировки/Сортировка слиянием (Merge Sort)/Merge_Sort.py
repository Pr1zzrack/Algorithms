def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Пример использования
arr = [38, 27, 43, 3, 9, 82, 10]
merge_sort(arr)
print("Отсортированный массив:", arr)


# Объяснение:

# def merge_sort(arr):: Определение функции сортировки слиянием.
# if len(arr) > 1:: Проверка, нужно ли сортировать массив. Если длина массива 1 или менее, он уже отсортирован.
# mid = len(arr) // 2: Находим середину массива.
# left_half = arr[:mid] и right_half = arr[mid:]: Разделяем массив на две половины.
# merge_sort(left_half) и merge_sort(right_half): Рекурсивно применяем сортировку слиянием к каждой половине.
# i = j = k = 0: Индексы для прохода по левой, правой и общей частям массива.
# while i < len(left_half) and j < len(right_half):: Объединяем две отсортированные половины в один массив.
# if left_half[i] < right_half[j]:: Сравниваем элементы из левой и правой частей.
# arr[k] = left_half[i] и arr[k] = right_half[j]: Помещаем меньший элемент из двух в общий массив.
# while i < len(left_half): и while j < len(right_half):: Проверяем, остались ли элементы в левой или правой части, и добавляем их в общий массив.