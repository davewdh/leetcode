class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        ans = -1
        for i in range(len(nums)):
            if count > nums[i]:
                ans = count + nums[i]
            count += nums[i]

        return ans

