class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        s = sum(nums)
        remain = s % p
        if remain == 0:
            return 0
        m = {0: -1} 
        prefixSum = 0
        ans = len(nums)

        for i in range(len(nums)):
            prefixSum += nums[i]
            temp = prefixSum % p
            prefix = (temp - remain + p) % p
            if prefix in m:
                l = i - m.get(prefix)
                ans = min(l, ans)
            m[temp] = i
            
        if ans == len(nums):
            return -1
        else:
            return ans