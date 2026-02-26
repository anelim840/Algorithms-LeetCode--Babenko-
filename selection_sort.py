def selection_sort(a):
    n = len(a)  #длина массива

    # проходим по массиву
    for i in range(n - 1):
        min_index = i  #считаем, что текущий элемент минимальный

        # ищем минимальный элемент в неотсортированной части
        for j in range(i + 1, n):
            if a[j] < a[min_index]:
                min_index = j #индекс нового минимума

        # меняем местами текущий элемент и найденный минимум
        a[i], a[min_index] = a[min_index], a[i]

    return a

arr = [64, 34, 25, 12, 22, 11, 90]
selection_sort(arr)
print(arr)