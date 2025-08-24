class Solution:
    def longestPalindrome(self, s: str) -> int:
        m = {}
        ans = 0
        for c in s:
            if m.get(c):
                m[c] += 1
            else:
                m[c] = 1
        odd_letter = False
        for v in m.values():
            if v % 2 == 0:
                ans += v
            else:
                if v > 1:
                    ans += (v-1)
                odd_letter = True
        if odd_letter:
            return ans + 1
        else:
            return ans