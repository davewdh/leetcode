class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = 0
        temp = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                temp += 1
            else:
                ans += ((temp * (temp + 1)) // 2)
                temp = 0
        ans += ((temp * (temp + 1)) // 2)
        return ans