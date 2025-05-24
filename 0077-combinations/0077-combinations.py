class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def dfs(start, curComb):
            if start > n:
                if len(curComb) == k:
                    ans.append(curComb.copy())
                return

            curComb.append(start)
            dfs(start + 1, curComb)
            curComb.pop()
            dfs(start + 1, curComb)

        dfs(1, [])

        return ans