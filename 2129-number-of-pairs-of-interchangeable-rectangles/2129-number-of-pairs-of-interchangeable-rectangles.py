class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        m = {}
        ans = 0
        for w, h in rectangles:
            if m.get(w/h):
                m[w/h] += 1
            else:
                m[w/h] = 1
        
        for v in m.values():
            if v > 1:
                ans += int((v * (v - 1)) / 2)
        return ans