# 中序遍历
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result=[]
        def inorder_Traversal(root,result):
            if root is not None:
                inorder_Traversal(root.left,result)
                result.append(root.val)
                inorder_Traversal(root.right,result)
        inorder_Traversal(root,result)    
        return result
