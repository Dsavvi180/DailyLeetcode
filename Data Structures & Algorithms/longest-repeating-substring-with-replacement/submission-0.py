class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        frequencyMap = {}
        maxFreq = 0
        longestSubstring = 0
        for right in range(len(s)):
            frequencyMap[s[right]] = frequencyMap.get(s[right],0)+1
            maxFreq = max(maxFreq, frequencyMap[s[right]])

            if right - left +1 - maxFreq >k: # because of this check the window will only ever have k replaced characters
                frequencyMap[s[left]]-=1
                left+=1
            
            longestSubstring = max(longestSubstring, right-left+1 )
        return longestSubstring

            
        
        