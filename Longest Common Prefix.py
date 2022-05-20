class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        # Edge Case
        if len(strs)==1:
            return strs[0]
        
        result=[] # List to capture the result
        # Time Complexity O(n) here n is the number of characters
        # Space Complexity  O(h) where h is the lenght of the minimum length word
    
        min_len=min([len(x) for x in strs])
        
        for i in range(min_len):
            if len(set([x[i] for x in strs]))==1:
                if strs[0][i]==strs[1][i]:
                    result.append(strs[0][i])
                else:
                    break
            else:
                break
        
        return "".join(result)