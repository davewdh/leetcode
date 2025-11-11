class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        temp = list(s)
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                if stack:
                    stack.pop()
                else:
                    temp[i] = ""

        while stack:
            temp[stack.pop()] = ""

        return "".join(temp)
            