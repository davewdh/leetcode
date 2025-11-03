class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        m = Counter(nums)
        ans = []

        while m:
            row = []
            temp = []
            for k, v in m.items():
                temp.append(k)
            for k in temp:
                row.append(k)
                m[k] -= 1
                if m[k] == 0:
                    m.pop(k)
            ans.append(row)
        return ans


            


            

