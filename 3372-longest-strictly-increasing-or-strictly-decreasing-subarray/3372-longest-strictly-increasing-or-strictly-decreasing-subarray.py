class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        ans = 1
        dec = 1
        inc = 1
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                inc += 1
                ans = max(inc, ans)
                ans = max(ans, dec)
                dec = 1
                print(ans)
            elif nums[i] > nums[i+1]:
                dec += 1
                ans = max(inc, ans)
                ans = max(ans, dec)
                inc = 1
            else:
                ans = max(inc, ans)
                ans = max(ans, dec)
                dec = 1
                inc = 1
        ans = max(inc, ans)
        ans = max(dec, ans)
        print(ans)
        return ans
                
            


            
