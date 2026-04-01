class Solution(object):
    def isValidBST(self, root):
        self.prev = None  

        def inorder(node):
            if node is None: 
                return True
            
            if not inorder(node.left):
                return False
            
            if self.prev is not None and node.val <= self.prev:
                return False  # если порядок нарушен
            
            self.prev = node.val # обновляем предыдущее значение

            return inorder(node.right)  # идем в правое поддерево
        
        return inorder(root)