class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False

        target = total // k 
        nums.sort(reverse=True)
        used = [False] * len(nums)

        def dfs(i, k, numSum):
            if k == 0:
                return True
            if numSum == target:
                return dfs(0, k - 1, 0)

            for j in range(i, len(nums)):
                if used[j] or numSum + nums[j] > target:
                    continue
                used[j] = True
                if dfs(j + 1, k, numSum + nums[j]):
                    return True
                used[j] = False

                if numSum == 0:
                    return False
            
            return False
        
        return dfs(0, k, 0)


            
