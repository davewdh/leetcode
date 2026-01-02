class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        l = 0

        for i in range(len(pushed)):
            stack.append(pushed[i])
            while stack and popped[l] == stack[-1]:
                stack.pop()
                l += 1
        if len(stack) > 0:
            return False
        return True