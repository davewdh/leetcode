class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        count0 = 0
        count1 = 0
        ans = 0

        for r in range(len(nums)):
            if nums[r] == 1:
                count1 += 1
            else:
                count0 += 1
            
            while count0 > k:
                if nums[l] == 0:
                    count0 -= 1
                l += 1
            
            ans = max(ans, r - l + 1)
        return ans

