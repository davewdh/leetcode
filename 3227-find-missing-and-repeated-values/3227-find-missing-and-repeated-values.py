class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        aMap = {}
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if aMap.get(grid[i][j]):
                    aMap[grid[i][j]] += 1
                else:
                    aMap[grid[i][j]] = 1
        r, m = 0, 0
        for i in range(1, n*n+1):
            if i not in aMap.keys():
                m = i
            if aMap.get(i) == 2:
                r = i
        return [r, m]
