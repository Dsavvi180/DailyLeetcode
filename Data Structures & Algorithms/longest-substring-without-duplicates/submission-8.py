class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) ==1:
            return 1
        left, right = 0, 1
        maxLen = 0
        duplicates = set(s[left])
        while left<right and right<len(s):
            if s[right] not in duplicates:
                duplicates.add(s[right])
                right+=1
            else:
                left+=1
                duplicates.clear()
                duplicates.add(s[left])
                right=left+1
            maxLen = max(maxLen,len(duplicates))
        return maxLen


        
                

        
       
        