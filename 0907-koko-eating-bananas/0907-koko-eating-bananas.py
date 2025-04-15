class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles) # k can be a [1, max(piles)]
        ans = r
        while l <= r:
            k = (l + r) // 2
            count = 0
            for p in piles:
                count += math.ceil(float(p) / k)
            if count <= h:
                ans = k
                r = k - 1
            else:
                l = k + 1
        return ans
