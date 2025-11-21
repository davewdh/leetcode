class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                nums[i-1] *= 2
                nums[i] = 0

        l = 0
        r = 1
        while r < len(nums):
            if nums[l] != 0:
                l += 1
                r += 1
            else:
                if nums[r] == 0:
                    r += 1
                    continue
                else:
                    nums[l], nums[r] = nums[r], nums[l]
                    l += 1
                    r += 1
        
        return nums
                    
            