class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        index = len(s) - 1
        for i in range(len(s)-1, -1, -1):
            if s[i] == " ":
                index -= 1
            else:
                break
        for i in range(index, -1, -1):
            if  s[i] != " ":
                count += 1
            else:
                break
        return count
            

            