class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1]
        for i in range(1, rowIndex+1):
            temp = ans[-1] * (rowIndex - i + 1) // i
            ans.append(temp)
        return ans
