class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        prefixSum1, prefixSum2 = grid[0].copy(), grid[1].copy()

        for i in range(1, len(grid[0])):
            prefixSum1[i] = prefixSum1[i] + prefixSum1[i - 1]
            prefixSum2[i] = prefixSum2[i] + prefixSum2[i - 1]

        ans = float("inf")
        for i in range(len(grid[0])):
            top = prefixSum1[-1] - prefixSum1[i]
            if i > 0:
                bottom = prefixSum2[i-1]
            else:
                bottom = 0
            ans = min(ans, max(top, bottom))
        return ans