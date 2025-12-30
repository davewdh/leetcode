class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        counter = Counter(s)
        if counter["a"] < k or counter["b"] < k or counter["c"] < k:
            return -1
        l = 0
        ans = 0

        for r in range(len(s)):
            counter[s[r]] -= 1

            while counter["a"] < k or counter["b"] < k or counter["c"] < k:
                counter[s[l]] += 1
                l += 1
            
            ans = max(ans, r-l+1)

        return len(s) - ans