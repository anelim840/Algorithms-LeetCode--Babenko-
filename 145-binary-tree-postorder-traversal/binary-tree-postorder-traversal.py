class Solution(object):
    def postorderTraversal(self, root):
        res = []

        def inorder(node):
            if node is None: # если узел пустой, выходим
                return
            
            inorder(node.left)     # идем в левое поддерево
            inorder(node.right)    # идем в правое поддерево
            res.append(node.val)   # добавляем значение узла
        
        inorder(root)
        return res
        