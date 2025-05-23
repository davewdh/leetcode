class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def dfs(i, curCombination, total):
            if total == target:
                ans.append(curCombination.copy())
                return
            if total > target or i >= len(candidates):
                return
            
            curCombination.append(candidates[i])
            dfs(i, curCombination, total + candidates[i])

            curCombination.pop()
            dfs(i + 1, curCombination, total)

        dfs(0, [], 0)
        return ans