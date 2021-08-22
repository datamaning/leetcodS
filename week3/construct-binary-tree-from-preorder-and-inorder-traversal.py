
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder)==0:
            return None
        root=TreeNode(preorder[0])
        idx=inorder.index(preorder[0])
        root.left=self.buildTree(preorder[1:idx+1],inorder[0:idx+1])
        root.right=self.buildTree(preorder[idx+1:],inorder[idx+1:])
        return root
