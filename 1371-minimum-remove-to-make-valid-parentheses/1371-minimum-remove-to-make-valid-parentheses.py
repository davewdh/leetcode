class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        temp = list(s)
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(s[i])
            elif s[i] == ")":
                if stack:
                    stack.pop()
                else:
                    temp[i] = ""

        temp1 = temp
        s1 = []
        for i in range(len(temp1)-1, -1 , -1):
            if temp1[i] == ")":
                s1.append(temp[i])
            elif temp1[i] == "(":
                if s1:
                    s1.pop()
                else:
                    temp1[i] = ""
        return "".join(temp1)
            