class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        ans = []
        m = {}
        for n in nums:
            if m.get(n):
                m[n] += 1
            else:
                m[n] = 1
        
        sorted_by_values = dict(sorted(m.items(), key=lambda item: item[1]))
        m1 = {}
        for k, v in sorted_by_values.items():
            if m1.get(v):
                m1[v].append(k)
                m1[v].sort(reverse=True)
            else:
                m1[v] = [k]
        s = dict(sorted(m1.items()))
        for k1, v1 in s.items():
            for n1 in v1:
                ans += [n1] * k1
        return ans