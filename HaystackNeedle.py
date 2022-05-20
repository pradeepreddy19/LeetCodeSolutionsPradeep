class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
         
            #Brute Force Solution
            l_hs=len(haystack)
            l_nd=len(needle)
            
            for i in range(l_hs):
                if haystack[i:i+l_nd]==needle:
                    return i
            return -1