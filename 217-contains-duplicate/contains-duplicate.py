class Solution(object):
    def containsDuplicate(self, nums):
        map = {} # создаем пустую хэш-таблицу
        
        for i in range(len(nums)):  # проходим по каждому элементу
            x = nums[i]
            
            if x in map: #если такое число есть в хэш-таблице, значит есть повтор 
                return True
            map[x] = 1 # иначе, записываем текущий элемент в хэш таблицу
        return False