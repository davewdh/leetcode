class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ans = 0
        b = True
        for s in words:
            for c in s:
                if c not in allowed:
                    b = False
                    break
            if b:
                ans += 1
            b = True
        return ans
            