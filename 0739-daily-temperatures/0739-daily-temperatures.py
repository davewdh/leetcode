class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = [] # (temp, index)
        ans = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while s and t > s[-1][0]:
                tS, iS = s.pop()
                ans[iS] = i - iS
            s.append((t, i))
        return ans