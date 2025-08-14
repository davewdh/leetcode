class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = {}
        ans = 0
        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1
        
        for v in count.values():
            if v > 1:
                ans += ((v * (v-1)) // 2)
        return ans