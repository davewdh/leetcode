class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        ans = []
        for key in count:
            if count[key] > len(nums) // 3:
                ans.append(key)
        return ans
            