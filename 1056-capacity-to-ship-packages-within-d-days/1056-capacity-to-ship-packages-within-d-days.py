class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        ans = r

        def canShip(cap):
            curCap = cap
            d = 1
            for w in weights:
                if curCap < w:
                    d += 1
                    curCap = cap
                curCap -= w
            return d <= days

        while l <= r:
            m = l + (r - l) // 2
            if canShip(m):
                r = m - 1
                ans = min(ans, m)
            else:
                l = m + 1
        return ans
