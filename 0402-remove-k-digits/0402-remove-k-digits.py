class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for n in num:
            while stack and k > 0 and stack[-1] > n:
                stack.pop()
                k -= 1
            
            stack.append(n)

        while k > 0:
            stack.pop()
            k -= 1
        
        i = 0
        while i < len(stack) and stack[i] == "0":
            i += 1

        ans = stack[i:]
        if ans:
            return "".join(ans)
        else:
            return "0"
           
