class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix, suffix, ans = [0] * n, [0] * n, [0] * n

        count = 0
        for i in range(n):
            count += nums[i]
            prefix[i] = count

        count2 = 0
        for j in range(n-1, -1, -1):
            count2 += nums[j]
            suffix[j] = count2

        for k in range(n):
            if k > 0:
                left = (nums[k] * k) - prefix[k-1]
            else:
                left = 0

            if k < n - 1:
                right = suffix[k+1] - (nums[k] * (n - k - 1))
            else:
                right = 0
            ans[k] = left + right

        return ans
            
            
            

