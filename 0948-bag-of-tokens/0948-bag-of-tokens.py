class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        n = len(tokens)
        l, r = 0, n - 1
        ans = 0

        while l <= r:
            if power >= tokens[l]:
                power -= tokens[l]
                ans += 1
                l += 1
            else:
                if ans > 0:
                    if l == r:
                        return ans
                    power += tokens[r]
                    ans -= 1
                    r -= 1
                else:
                    return ans
        return ans

