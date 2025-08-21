class Solution:
    def maxScore(self, s: str) -> int:
        ans = 0
        ones = s.count("1")
        zeros = 0
        if s[0] == "0":
            zeros = 1
        else:
            ones -= 1
        ans = max(ans, zeros + ones)
        for i in range(1, len(s)-1):
            if s[i] == "0":
                zeros += 1
            else:
                ones -= 1
            ans = max(ans, zeros + ones)
        return ans