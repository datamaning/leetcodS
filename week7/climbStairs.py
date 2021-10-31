
oclass Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:return n
        f_1, f_2 = 1, 2
        f = 0
        for i in range(2, n):
            f = f_1 + f_2
            f_1 = f_2  
            f_2 = f
        
        return f

