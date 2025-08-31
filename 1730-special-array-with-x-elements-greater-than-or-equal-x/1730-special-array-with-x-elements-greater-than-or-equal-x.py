class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        prev = 0
        for i in range(len(nums)):
            temp = prev + 1
            while temp <= nums[i]:
                if temp == (len(nums) - i):
                    return temp
                temp += 1
            prev = nums[i]
        return -1