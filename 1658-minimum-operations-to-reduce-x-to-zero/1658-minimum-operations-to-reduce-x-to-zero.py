class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        if target == 0:
            return len(nums)
        l, r = 0, 0
        max_window = 0
        s = 0

        while r < len(nums):
            s += nums[r]
            while l <= r and s > target:
                s -= nums[l]
                l += 1
            if s == target:
                max_window = max(max_window, r - l + 1)
            r += 1
        if max_window:
            return len(nums) - max_window
        else:
            return -1
