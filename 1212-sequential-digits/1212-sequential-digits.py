class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        s = "123456789"
        l = len(str(low))
        h = len(str(high))
        ans = []
        for i in range(l, h+1):
            for j in range(0, len(s)-i+1):
                temp = int(s[j:j+i])
                if low <= temp <= high:
                    ans.append(temp)
        return ans

