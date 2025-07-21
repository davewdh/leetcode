class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ptrS, ptrT = 0, 0
        while ptrS < len(s) and ptrT < len(t):
            if s[ptrS] == t[ptrT]:
                ptrS += 1
        
            ptrT += 1

        if ptrS < len(s):
            return False
        return True