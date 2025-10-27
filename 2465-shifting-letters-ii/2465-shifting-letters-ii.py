class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        aList = [0] * (len(s) + 1)

        for start, end, direction in shifts:
            if direction == 1:
                aList[start] += 1
                aList[end+1] -= 1
            else:
                aList[start] -= 1
                aList[end+1] += 1

        temp = []
        for c in s:
            temp.append(ord(c) - ord("a"))

        prefixSum = 0
        for i in range(len(temp)):
            prefixSum += aList[i]
            temp[i] = ((temp[i] + prefixSum) + 26)%26

        temp2 = []
        for n in temp:
            temp2.append(chr(n + ord("a")))
        return "".join(temp2)


