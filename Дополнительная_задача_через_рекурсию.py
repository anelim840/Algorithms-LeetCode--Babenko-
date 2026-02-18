def search(nums, target, first, last):
    if first > last: 
        return -1  # выводим -1 потому что элемент отсутсвует, т к он не найден после проверки каждого элемента
    
    mid = (left + right) // 2 # находим середину текущего диапазона
    
    if nums[mid] == target:
        return mid #элемент найден -> возвращаем индекс


    elif nums[mid] < target:
        return search(nums, target, mid + 1, last)  # если элемент посередине меньше искомого "таргет", ищем дальше в правой части 

   
    else:
        return search(nums, target, first, mid - 1)  # если элемент посередине больше искомого "таргет", ищем дальше в левой части 