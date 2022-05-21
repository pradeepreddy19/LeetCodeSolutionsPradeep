class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums=sorted(nums)
        value=0
        for i in range(0,len(nums),2):
            value+=nums[i]
        return value
            