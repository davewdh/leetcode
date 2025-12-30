class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        l = 0
        ans = 0
        aMap = {}

        for r in range(len(nums)):
            if aMap.get(nums[r]):
                aMap[nums[r]] += 1
            else:
                aMap[nums[r]] = 1

            while aMap.get(nums[r]) > k:
                aMap[nums[l]] -= 1
                if aMap[nums[l]] == 0:
                    aMap.pop(nums[l])
                l += 1

            ans = max(ans, r - l + 1)
        return ans