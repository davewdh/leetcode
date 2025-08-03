class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        s = 0
        for i in range(len(nums)):
            if (total - nums[i]) / 2 == s:
                return i
            else:
                s += nums[i]
        return -1