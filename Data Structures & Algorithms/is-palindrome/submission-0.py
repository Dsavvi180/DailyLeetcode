class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = list(s.lower())
        n = len(s)
        for i in range(n):
            if not s[i].isalnum():
                s[i] = ""
        s = "".join(s)
        n = len(s)
        
        for i in range(n//2):
            j = n-1-i
            if s[i]!=s[j]:
                return False
        return True
            
        