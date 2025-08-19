class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = -1
        for i in range(len(num)-2):
            temp = num[i:i+3]
            if len(set(temp)) > 1:
                continue
            else:
                ans = max(ans, int(temp[0]))

        if ans > 0:
            return str(ans) * 3
        elif ans == 0:
            return "000"
        else:
            return ""
