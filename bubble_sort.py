def bubble_sort(A):
    n = len(A)  # длина массива

    for i in range(1, n): #проходим каждый элемент

        for j in range(n - 1, i - 1, -1): # сравниваем соседние элементы и при необходимости меняем их местами

            # еслм правый меньше, меняем местами
            if A[j] < A[j - 1]:
                A[j], A[j - 1] = A[j - 1], A[j]

    return A


arr = [5, 1, 4, 2, 8]
bubble_sort(arr)
print(arr)
