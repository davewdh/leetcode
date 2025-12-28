class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        l = 0
        count = 0
        ans = 0
         
        for r in range(len(s)):
            count += abs(ord(s[r]) - ord(t[r]))

            while count > maxCost:
                count -= abs(ord(s[l]) - ord(t[l]))
                l += 1

            ans = max(r - l + 1, ans)
        
        return ans