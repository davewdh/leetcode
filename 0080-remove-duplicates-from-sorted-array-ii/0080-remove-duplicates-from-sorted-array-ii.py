class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ans = 0
        l = 0
        n = len(nums)
        while l < n:
            temp = 1
            num = nums[l]
            while l < n - 1 and nums[l] == nums[l+1]:
                temp += 1
                l += 1

            nums[ans] = num
            ans += 1

            if temp > 1:
                nums[ans] = num
                ans += 1
            l += 1

        return ans