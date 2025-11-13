class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        m = {}
        n = len(nums)
        total = (n * (n-1)) // 2
        good_pairs = 0

        for i, n in enumerate(nums):
            temp = n - i
            if m.get(temp):
                m[temp] += 1
            else:
                m[temp] = 1

        for k, v in m.items():
            if v > 1:
                good_pairs += ((v * (v-1)) // 2)
        return total - good_pairs