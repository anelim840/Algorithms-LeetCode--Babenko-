import random

def partition(arr, low, high):
    pivot = arr[high] # опорный элемент
    i = low - 1 # граница для элементов <= pivot

    for j in range(low, high): #проходимся по всем элементам, кроме pivot
        if arr[j] <= pivot: # если текущий элемент меньше или равен pivot
            i += 1 #двигаем указатель вправо
            arr[i], arr[j] = arr[j], arr[i] #даем элементу меньше pivot новый индекс, так как элемент меньше pivot и должен находиться с левой стороны

    arr[i + 1], arr[high] = arr[high], arr[i + 1] # ставим pivot на правильную позицию

    return i + 1 #новый индекс   pivot


def quick_sort(arr, low, high):
 
    if low < high:
        
        random_index = random.randint(low, high) # выбираем случайный индекс для pivot
        arr[random_index], arr[high] = arr[high], arr[random_index] #делаем случайный элемент последним, меняя их местами

        q = partition(arr, low, high) #разбиваем подмасссив вокруг pivot
        quick_sort(arr, low, q - 1)# рекурсивно сортируем левую часть
        quick_sort(arr, q+1, high) # рекурсивно сортируем правую часть

arr = [5, 8, 2, 6, 11, 1, 7]
quick_sort(arr, 0, len(arr) - 1)
print (arr)