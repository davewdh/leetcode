class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        l = 0
        ans = ""
        for i in range(len(s)):

            if l < len(spaces) and (spaces[l] == 0 or i == spaces[l]):
                ans += " "
                l += 1
            ans += s[i]
        return ans