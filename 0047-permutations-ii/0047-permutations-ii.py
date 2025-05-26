class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        count = {n:0 for n in nums}
        for n in nums:
            count[n] += 1

        perm = []

        def dfs():
            if len(perm) == len(nums):
                ans.append(perm.copy())
                return

            for n in count:
                if count[n] > 0:
                    perm.append(n)
                    count[n] -= 1
                    dfs()
                    count[n] += 1
                    perm.pop()
        
        dfs()
        return ans
        
