class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        l, r = 0, 0
        w1, w2 = "", ""
        while l < len(word1) and r < len(word2):
            w1 += word1[l]
            w2 += word2[r]
            l += 1
            r += 1
        
        while l < len(word1):
            w1 += word1[l]
            l += 1
        
        while r < len(word2):
            w2 += word2[r]
            r += 1

        return w1 == w2