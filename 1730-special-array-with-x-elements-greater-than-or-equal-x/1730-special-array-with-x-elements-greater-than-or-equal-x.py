class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        prev = 0
        for i in range(len(nums)):
            for j in range(prev+1, nums[i]+1):
                if j == (len(nums) - i):
                    return j
            prev = nums[i]
        return -1