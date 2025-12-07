class Solution:
    def minimumLength(self, s: str) -> int:
        n = len(s)
        ans = n
        l, r = 0, n - 1
        while l < r and s[l] == s[r]:
            temp = s[l]
            while l <= r and s[l] == temp:
                    l += 1
            while l <= r and s[r] == temp:
                    r -= 1
        return r - l + 1
    