class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split(" ")
        ans = ""
        for i, w in enumerate(arr):
            l, r = 0, len(w) - 1
            temp = list(w)
            while l < r:
                temp[l], temp[r] = temp[r], temp[l]
                l += 1
                r -= 1
            if i == len(arr) - 1:
                ans = ans + "".join(temp)
            else:
                ans = ans + "".join(temp) + " "
        return ans
