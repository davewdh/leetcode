class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        index = len(s) - 1
        while s[index] == " ":
            index -= 1
        while s[index] != " " and index >= 0:
            index -= 1
            count += 1
        return count
            

            