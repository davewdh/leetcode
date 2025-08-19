class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ans = 0
        for s in words:
            b = True
            for c in s:
                if c not in allowed:
                    b = False
                    break
            if b:
                ans += 1
        return ans
            