class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_len=0
        for i,distance in enumerate(nums):
            if max_len>=i and (i+distance)>max_len:
                max_len=i+distance
        return max_len>=i


