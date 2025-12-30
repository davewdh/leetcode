class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        m = max(nums)
        l = 0
        count = 0
        ans = 0

        for r in range(len(nums)):
            if nums[r] == m:
                count += 1
            
            while count >= k:
                if nums[l] == m:
                    count -= 1
                l += 1
            ans += l

        return ans