class Solution(object):
    def insertIntoBST(self, root, val):
        if not root:
            return TreeNode(val)  # создаем новый узел
        
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)  # идем влево
        else:
            root.right = self.insertIntoBST(root.right, val)  # идем вправо
        
        return root  # возвращаем корень
        