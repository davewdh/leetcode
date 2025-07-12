class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        base1 = 1
        base2 = 2
        ans = 0
        for i in range(2, n):
            ans = base1 + base2
            base1 = base2
            base2 = ans

        return ans
