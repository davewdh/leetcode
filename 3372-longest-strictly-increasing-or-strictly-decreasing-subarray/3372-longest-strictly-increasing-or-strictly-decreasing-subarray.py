class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        ans = 1
        dec = 1
        inc = 1
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                inc += 1
                dec = 1
            elif nums[i] > nums[i+1]:
                dec += 1
                inc = 1
            else:
                dec = 1
                inc = 1
            ans = max(inc, ans, dec)
        return ans
                
            


            
