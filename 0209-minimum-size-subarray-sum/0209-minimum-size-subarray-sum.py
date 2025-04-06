class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #  2,3,1,2,4,3.   target = 7
        #  lr
        l = 0
        s = 0
        ans = len(nums) + 1 # invaid ans
        for r in range(len(nums)):
            s += nums[r]

            while s >= target:
                s -= nums[l]
                ans = min(ans, r - l + 1)
                l += 1

        if ans > len(nums):
            return 0
        else:
            return ans