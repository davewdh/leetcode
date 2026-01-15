class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        ans = 0
        for i in range(len(s)-1, -1 , -1):
            if s[i] == ")":
                stack.append(s[i])
            else:
                if stack:
                    stack.pop()
                else:
                    ans += 1
        return ans + len(stack)