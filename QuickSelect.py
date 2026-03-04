import random
# по Ломуто
def partition(arr, low, high):
    pivot = arr[high] # опорный элемент
    i = low - 1 # граница для элементов <= pivot

    for j in range(low, high): #проходимся по всем элементам, кроме pivot
        if arr[j] <= pivot: # если текущий элемент меньше или равен pivot
            i += 1 #двигаем указатель вправо
            arr[i], arr[j] = arr[j], arr[i] #даем элементу меньше pivot новый индекс, так как элемент меньше pivot и должен находиться с левой стороны

    arr[i + 1], arr[high] = arr[high], arr[i + 1] # ставим pivot на правильную позицию

    return i + 1 #новый индекс   pivot



# QuickSelect
def quick_select(arr, k):
    if k < 0 or k >= len(arr):
        raise ValueError #k должен находиься в массиве
    
    low = 0 #левая граница
    high = len(arr) - 1 #правая граница

    while low <= high: #проверяем, если в массиве элемента и есть смысл его сортировать


        random_index = random.randint(low, high)  # выбираем случайный индекс для pivot
        arr[random_index], arr[high] = arr[high], arr[random_index]#делаем случайный элемент последним, меняя их местами

       
        q = partition(arr, low, high)

        if q == k:
            #то и есть k-й наименьший элемент
            return arr[q]

        elif k < q:  # k меньше pivot, значит находится слева
            high = q - 1 #тогда продолжаем поиск только в левой части

        else: # k больше pivot, значит находится справа
            low = q + 1 #тогда продолжаем поиск только в правой части


arr = [5, 8, 2, 6, 11, 1, 7, 7, 20]
k = 5
print("Исходный массив:", arr)
print("k:", k)
result = quick_select(arr, k)
print( "k-й наименьший элемент:", result)