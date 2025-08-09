class Solution:
    def findLucky(self, arr: List[int]) -> int:
        m = {}
        for n in arr:
            if n in m:
                m[n] += 1
            else:
                m[n] = 1
        luck = -1
        for k, v in m.items():
            if k == v:
                luck = max(luck, k)
        return luck
