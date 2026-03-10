import random
#сортировка вставками
def insertion_sort(arr):
    for i in range(1, len(arr)): #начинаем со второго элемента, потому что считаем первый элемент уже отсортированным
        key = arr[i] #ключ который будем вставляь в правильное место
        j = i - 1 #индекс последнего элемента в отсортированной части
        while j >= 0 and arr[j] > key: # 
            arr[j + 1] = arr[j] #сдвигаем элементы которые больше ключа в право
            j -= 1 #переходим к прерылущему элементу
        arr[j + 1] = key #вставляем ключ на правильное место

    return arr


# быстрая сортировка по Ломуто
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
 
    if low < high: # проверяем, если в массиве больше одного элемента и есть смысл его сортировать
        
        random_index = random.randint(low, high) # выбираем случайный индекс для pivot
        arr[random_index], arr[high] = arr[high], arr[random_index] #делаем случайный элемент последним, меняя их местами

        q = partition(arr, low, high) #разбиваем подмасссив вокруг pivot
        quick_sort(arr, low, q - 1)# рекурсивно сортируем левую часть
        quick_sort(arr, q+1, high) # рекурсивно сортируем правую часть
