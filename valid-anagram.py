
# 第一种方法，排序后统计
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s_counter=collections.Counter(s)
        t_counter=collections.Counter(t)
        for key,value in s_counter.items():
            t_value=t_counter.get(key,0)
            if t_value!=value:
                return False
        return True
