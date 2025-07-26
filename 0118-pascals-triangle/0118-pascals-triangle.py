class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        for i in range(1, numRows):
            row = [1]
            pre = ans[-1]
            print(pre)
            for j in range(0, len(pre)-1):
                row.append(pre[j] + pre[j+1])
            row.append(1)
            ans.append(row)
        return ans
