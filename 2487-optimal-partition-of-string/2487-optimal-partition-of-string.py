class Solution:
    def partitionString(self, s: str) -> int:
        temp = set()
        ans = 1
        for c in s:
            if c in temp:
                ans += 1
                temp.clear()
            
            temp.add(c)
        return ans