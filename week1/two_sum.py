class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for index,seq in enumerate(nums) :
            hashmap[seq]=index
        for i in range(len(nums)):
            j=hashmap.get(target-nums[i])
            if j is not None and i!=j:
                return [i,j]
