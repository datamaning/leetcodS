class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        # 结果
        result=[]
        def pre_order(root):
            if root is not None:
                result.append(root.val)
                for child in root.children:
                    pre_order(child)
        pre_order(root)
        return result
