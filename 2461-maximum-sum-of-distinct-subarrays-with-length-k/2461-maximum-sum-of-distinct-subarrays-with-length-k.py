class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        l = 0
        ans = 0
        aMap = {}
        count = 0

        for r in range(len(nums)):
            count += nums[r]
            if aMap.get(nums[r]):
                aMap[nums[r]] += 1
            else:
                aMap[nums[r]] = 1

            if r-l+1 > k:
                aMap[nums[l]] -= 1
                if aMap[nums[l]] == 0:
                    aMap.pop(nums[l])
                count -= nums[l]
                l += 1
            
            if r-l+1 == k:
                if len(aMap) == k:
                    ans = max(ans, count)
        return ans