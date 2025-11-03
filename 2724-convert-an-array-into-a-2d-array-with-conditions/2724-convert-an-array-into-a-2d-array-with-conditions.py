class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        m = Counter(nums)
        ans = []

        while m:
            row = []
            for k in list(m.keys()):
                row.append(k)
                m[k] -= 1
                if m[k] == 0:
                    m.pop(k)
            ans.append(row)
        return ans


            


            

