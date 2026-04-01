class Solution(object):
    def inorderTraversal(self, root):
        res = []

        def inorder(node):
            if node is None: # если узел пустой, выходим
                return
            
            inorder(node.left)     # идем в левое поддерево
            res.append(node.val)   # добавляем значение узла
            inorder(node.right)    # идем в правое поддерево
        
        inorder(root)
        return res