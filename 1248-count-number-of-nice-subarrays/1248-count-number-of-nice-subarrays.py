class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def helper(x):
            l = 0
            ans = 0
            count = 0

            for r in range(len(nums)):
                if nums[r] % 2 == 1:
                    count += 1
                
                while count > x:
                    if nums[l] % 2 == 1:
                        count -= 1
                    l += 1

                ans += (r - l + 1)
            return ans
        
        return helper(k) - helper(k - 1)