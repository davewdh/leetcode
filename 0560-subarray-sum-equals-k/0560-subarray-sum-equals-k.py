class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        curSum = 0
        prefixSums = {0: 1}
        for num in nums:
            curSum += num
            diff = curSum - k
            if diff in prefixSums:
                ans += prefixSums[diff]

            if curSum in prefixSums:
                prefixSums[curSum] += 1
            else:
                prefixSums[curSum] = 1
        return ans
