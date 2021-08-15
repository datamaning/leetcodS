"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        result=[]
        queue=[root]
        if root is None:
            return []

        while queue:
            lenQ=len(queue) #获取队列长度
            sub=[]
            for i in range(lenQ):
                valKey=queue.pop(0) #获取队首元素
                if valKey:
                    sub.append(valKey.val)  #加入sub列
                    if valKey.children:
                        queue.extend(valKey.children)
            result.append(sub)
        return result
