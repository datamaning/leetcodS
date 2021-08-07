class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=len(digits)
        final=0
        for i in range(n):
            final=10*final+digits[i]
        final=final+1
        finalStr=str(final)
        return list(map(int,list(finalStr)))
