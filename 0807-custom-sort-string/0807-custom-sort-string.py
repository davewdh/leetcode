class Solution:
    def customSortString(self, order: str, s: str) -> str:
        m = {}
        ans = ""
        for c in s:
            if m.get(c):
                m[c] += 1
            else:
                m[c] = 1
        for c in order:
            if m.get(c):
                ans += (c * m.get(c))
                del m[c]
        for k, v in m.items():
            ans += (k * v)
        return ans
