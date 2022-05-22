class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        max_ones=0
        temp_ones=0
        
        for each in nums:
            if each==1:
                temp_ones+=1
            else:
                max_ones=max(max_ones,temp_ones)
                temp_ones=0
        return max(max_ones,temp_ones)
                
        