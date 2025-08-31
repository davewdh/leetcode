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
            ans += [n1] * m.pop(n1)
        
        for k in sorted(m):
            ans += [k] * m[k]
        return ans