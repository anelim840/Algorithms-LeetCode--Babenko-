class Solution(object):
    def preorderTraversal(self, root):
        res = []

        def inorder(node):
            if node is None: # если узел пустой, выходим
                return
            
            res.append(node.val)   # добавляем значение узла
            inorder(node.left)     # идем в левое поддерево
            inorder(node.right)    # идем в правое поддерево
        
        inorder(root)
        return res