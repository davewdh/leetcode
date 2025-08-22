class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n = len(words)
        if n <= 1:
            return True
        m = {}
        for w in words:
            for c in w:
                if m.get(c):
                    m[c] += 1
                else:
                    m[c] = 1

        for v in m.values():
            if v % n != 0:
                return False
        return True