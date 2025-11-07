class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        ans = -1
        for i in range(len(nums)):
            if i >=2 and count > nums[i]:
                ans = count + nums[i]
                print(ans)
            count += nums[i]

        return ans

