class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        aMap = defaultdict(int)
        n = len(grid)

        for i in range(n):
            for j in range(n):
                aMap[grid[i][j]] += 1

        m, r = 0, 0
        for i in range(1, n * n + 1):
            if aMap[i] == 2:
                r = i
            if aMap[i] == 0:
                m = i

        return [r, m]
