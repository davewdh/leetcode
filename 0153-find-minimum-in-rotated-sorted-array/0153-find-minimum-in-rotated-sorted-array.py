class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] <= nums[r]:
                r = m
            else:
                l = l + 1
        return nums[l]
        

        # 4,5,6,7,0,1,2