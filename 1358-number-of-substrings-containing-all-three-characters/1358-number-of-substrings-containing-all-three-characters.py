class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l = 0
        ans = 0
        aMap = {}

        for r in range(len(s)):
            if aMap.get(s[r]):
                aMap[s[r]] += 1
            else:
                aMap[s[r]] = 1

            while len(aMap) == 3:
                ans += (1 + len(s) - r - 1)
                aMap[s[l]] -= 1
                if aMap[s[l]] == 0:
                    aMap.pop(s[l])
                l += 1

        return ans