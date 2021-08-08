class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow,high=0,0
        while high<len(nums):
            if nums[high]!=0:
                nums[high],nums[slow]=nums[slow],nums[high]
                slow+=1
            high+=1
        return nums
