class Solution(object):
    def floodFill(self, image, sr, sc, color):
        fcolor = image[sr][sc]
        
        if fcolor == color:
            return image
        
        def dfs(r, c): # проверка границ
            if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]):
                return
            
            if image[r][c] != fcolor:
                return
            
            image[r][c] = color # если не тот цвет, то красим
            
            dfs(r+1, c) #вниз
            dfs(r-1, c) #вверх
            dfs(r, c+1) #вправо
            dfs(r, c-1) #влево
        
        dfs(sr, sc)
        return image
        