class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backTracking(s: str, openN: int, closeN: int):
            if len(s) == 2 * n:
                ans.append(s)
                return
            if openN < n:
                backTracking(s + '(', openN + 1, closeN)
            if closeN < openN:
                backTracking(s + ')', openN, closeN + 1)
        
        backTracking('', 0, 0)
        return ans