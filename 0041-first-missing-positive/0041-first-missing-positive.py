class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        nums.sort()
        missing = 1
        for num in nums:
            if num > 0 and num == missing:
                missing += 1
        return missing
        