class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        # 3[a]2[bc] 3  , subStr = a, pop one more time, k = pop(), append k * substr
        # aaa a [ b c , subStr = subStr + pop(), bc, k = pop(), bcbc
        # aaa bcbc
        for c in s:
            if c == ']':
                subStr = ''
                while stack and stack[-1] != '[':
                    subStr = stack.pop() + subStr
                stack.pop()
                k = ''
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append((int(k) * subStr))
            else:
                stack.append(c)
        return ('').join(stack)
