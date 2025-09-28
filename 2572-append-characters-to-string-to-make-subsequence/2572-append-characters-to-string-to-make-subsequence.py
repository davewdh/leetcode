class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        ans = len(t)
        for c in t:
            if c in s:
                ans -= 1
                s = s[s.index(c)+1:]
            else:
                return ans
        return ans


        
  
            