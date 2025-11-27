class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1
        ans = 0
        mod = 10**9 + 7
        nums.sort()
        while l <= r:
            if nums[l] + nums[r] <= target:
                ans = (ans + pow(2, r-l, mod)) % mod
                l += 1
            else:
                r -= 1
        return ans
