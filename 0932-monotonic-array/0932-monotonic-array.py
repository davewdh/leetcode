class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                for j in range(i+1, n-1):
                    if nums[j] < nums[j+1]:
                        return False
                return True
            elif nums[i] < nums[i+1]:
                for j in range(i+1, n-1):
                    if nums[j] > nums[j+1]:
                        return False
                return True
        return True

