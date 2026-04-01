class Solution(object):
    def preorderTraversal(self, root):
        res = []

        def preorder(node):
            if node is None: # если узел пустой, выходим
                return
            
            res.append(node.val)   # добавляем значение узла
            preorder(node.left)     # идем в левое поддерево
            preorder(node.right)    # идем в правое поддерево
        
        preorder(root)
        return res