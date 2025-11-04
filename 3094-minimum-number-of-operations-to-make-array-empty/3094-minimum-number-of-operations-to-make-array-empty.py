class Solution:
    def minOperations(self, nums: List[int]) -> int:
        m = Counter(nums)
        ans = 0
        for k, v in m.items():
            if v == 1:
                return -1
            ans += ceil(v / 3)

        return ans