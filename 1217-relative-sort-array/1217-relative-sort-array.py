class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        m = {}
        ans = []
        for n in arr1:
            if m.get(n):
                m[n] += 1
            else:
                m[n] = 1
        
        for n1 in arr2:
            if m.get(n1):
                for i in range(m.get(n1)):
                    ans.append(n1)
            m.pop(n1)
        
        for k, v in sorted(m.items()):
            for j in range(v):
                ans.append(k)
        return ans