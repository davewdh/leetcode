class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l = 0
        ans = 0
        v = {'a', 'e', 'i', 'o', 'u'}
        count = 0
        for r in range(len(s)):
            if s[r] in v:
                count += 1
            
            if (r - l + 1) == k:
                ans = max(ans, count)
                if s[l] in v:
                    count -= 1
                l += 1
        return ans
