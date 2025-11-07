class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        ans = -1
        if nums[0] + nums[1] > nums[2]:
            ans = nums[0] + nums[1] + nums[2]
        
        count = nums[0] + nums[1] + nums[2]
        for i in range(3, len(nums)):
            if count > nums[i]:
                ans = count + nums[i]
                print(ans)
            count += nums[i]

        return ans

