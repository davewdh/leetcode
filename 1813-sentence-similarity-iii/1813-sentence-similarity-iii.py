class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s1 = sentence1.split(" ")
        s2 = sentence2.split(" ")
        if len(s1) > len(s2):
            s1, s2 = s2, s1
        l, r1, r2 = 0, len(s1) -1, len(s2)-1
        prefix, suffix = "", ""
        while l <= r1 and s1[l] == s2[l]:
            prefix += s1[l]
            l += 1
        while l <= r1 and s1[r1] == s2[r2]:
            temp = s1[r1] + suffix
            suffix  = temp
            r1 -= 1
            r2 -= 1
            
        if (prefix + suffix) == "".join(s1):
            return True
        else:
            return False
      