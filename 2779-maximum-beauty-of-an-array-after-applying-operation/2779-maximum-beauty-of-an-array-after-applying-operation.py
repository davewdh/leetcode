class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        if nums[-1] == nums[0]:
            return len(nums)
        l = 0
        ans = 1

        for r in range(len(nums)):

            while nums[r] - nums[l] > 2 * k:
                l += 1
            
            ans = max(ans, r-l+1)

        return ans
