class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        pre_sum = 0
        odd = 0
        even = 0
        ans = 0
        mod = 10**9 + 7

        for n in arr:
            pre_sum += n
            if pre_sum % 2 == 1:
                ans = (1 + ans + even) % mod
                odd += 1
            else:
                ans = (ans + odd) % mod
                even += 1
        return ans 