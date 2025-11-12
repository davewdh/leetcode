class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        one, zero, ans = 0, 0, 0
        m = {}

        for i, n in enumerate(nums):
            if n == 0:
                zero += 1
            else:
                one += 1

            diff = one - zero
            if diff not in m:
                m[diff] = i

            if one == zero:
                ans = one + zero
            else:
                index = m[diff]
                ans = max(ans, i - index)
        return ans
