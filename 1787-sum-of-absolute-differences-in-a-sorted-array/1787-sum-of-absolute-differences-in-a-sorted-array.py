class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        total = sum(nums)
        prefix = 0

        for i, num in enumerate(nums):
            total -= num
            left = (num * i) - prefix
            right = total - (num * (n-i-1))
            ans[i] = left + right
            prefix += num

        return ans
            
            
            

