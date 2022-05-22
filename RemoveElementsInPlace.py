class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        for i in range(len(nums)):
            if nums[i]==val:
                nums[i]=None
                
        left=None
        right=None
        for i in range(len(nums)):
            if nums[i]==None and left==None:
                left=i
            elif left!=None and nums[i]!=None:
                right=i
                break
                
        print(left,right)     
        if left!=None and right!=None:
            while right<len(nums):
                if nums[left]==None and nums[right]!=None:
                    nums[left],nums[right]=nums[right],nums[left]
                    left+=1
                    right+=1
                else:
                    if nums[left]!=None:
                        left+=1
                    if nums[right]==None:
                        right+=1
                
                
        for each in nums[::-1]:
            if each==None:
                nums.pop()
            else:
                break


            
            
                
        
        
        
        
        
            
            
        