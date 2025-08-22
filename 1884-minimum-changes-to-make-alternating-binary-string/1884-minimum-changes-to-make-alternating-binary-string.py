class Solution:
    def minOperations(self, s: str) -> int:
        ans1 = 0
        ans2 = 0
        for i in range(len(s)):
            # 101010101...
            if i % 2 != 0:
                if s[i] == "0":
                    ans1 += 1
                if s[i] == "1":
                    ans2 += 1
            else:
                if s[i] == "1":
                    ans1 += 1
                if s[i] == "0":
                    ans2 += 1

        return min(ans1, ans2)
        