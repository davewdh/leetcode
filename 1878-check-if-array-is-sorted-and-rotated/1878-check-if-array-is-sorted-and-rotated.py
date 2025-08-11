class Solution:
    def check(self, nums: List[int]) -> bool:
        skip = 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                skip += 1
                if skip > 1:
                    return False
                if (nums[i+1:] + nums[:i+1]) != sorted(nums):
                    return False
        return True