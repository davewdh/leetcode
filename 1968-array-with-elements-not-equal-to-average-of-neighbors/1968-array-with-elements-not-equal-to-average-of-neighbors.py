class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums) - 2):
            if (nums[i-1] + nums[i+1]) ==  2 * nums[i]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
        
        for j in range(len(nums) - 2, 0, -1):
            if (nums[j-1] + nums[j+1]) ==  2 * nums[j]:
                nums[j], nums[j-1] = nums[j-1], nums[j]
        return nums
