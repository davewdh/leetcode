class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pac = set()
        atl = set()
        ans = []

        def dfs(r, c, visited, preHeight):
            if r < 0 or r == rows or c < 0 or c == cols or (r, c) in visited or heights[r][c] < preHeight:
                return 
            visited.add((r, c))
            dfs(r+1, c, visited, heights[r][c])
            dfs(r-1, c, visited, heights[r][c])
            dfs(r, c+1, visited, heights[r][c])
            dfs(r, c-1, visited, heights[r][c])



        for r in range(rows):
            dfs(r, 0, pac, heights[r][0]) #preHeight
            dfs(r, cols - 1, atl, heights[r][cols - 1])

        for c in range(cols):
            dfs(0, c, pac, heights[0][c]) #preHeight
            dfs(rows - 1, c, atl, heights[rows - 1][c])

        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    ans.append([r, c])
        return ans
