class Solution(object):
    def containsDuplicate(self, nums):
        d = {} # создаем пустую хэш-таблицу
        
        for i in range(len(nums)):  # проходим по каждому элементу
            x = nums[i]
            
            if x in d: #если такое число есть в хэш-таблице, значит есть повтор 
                return True
            d [x] = 1 # иначе, записываем текущий элемент в хэш таблицу
        return False