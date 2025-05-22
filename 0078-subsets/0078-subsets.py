class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        temSubset = []
        def dfs(i):
            if i >= len(nums):
                ans.append(temSubset.copy())
                return
            
            temSubset.append(nums[i])
            dfs(i + 1)

            temSubset.pop()
            dfs(i + 1)

        dfs(0)

        return ans

