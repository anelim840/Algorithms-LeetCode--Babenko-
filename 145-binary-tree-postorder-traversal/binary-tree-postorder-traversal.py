class Solution(object):
    def postorderTraversal(self, root):
        res = []

        def postorder(node):
            if node is None: # если узел пустой, выходим
                return
            
            postorder(node.left)     # идем в левое поддерево
            postorder(node.right)    # идем в правое поддерево
            res.append(node.val)   # добавляем значение узла
        
        postorder(root)
        return res
        