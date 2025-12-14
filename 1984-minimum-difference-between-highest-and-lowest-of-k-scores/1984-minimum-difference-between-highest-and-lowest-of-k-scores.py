class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        r = k - 1
        ans = nums[r] - nums[l]
        l += 1
        for r in range(k, len(nums)):
            ans = min(nums[r] - nums[l], ans)
            l += 1
            r += 1
        return ans