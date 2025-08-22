class Solution:
    def minOperations(self, s: str) -> int:
        ans1 = 0
        ans2 = 0
        for i in range(len(s)):
            if s[i] == "0":
                if i % 2 != 0:
                    ans1 += 1
                else:
                    ans2 += 1
            else:
                if i % 2 != 0:
                    ans2 += 1
                else:
                    ans1 += 1
        return min(ans1, ans2)
        