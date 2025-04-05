class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        #  "ab", s2 = "eidbaooo"
        # hashmap, 26.   a: 1, b, 1, c
        s1count, s2count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1count[ord(s1[i]) - ord("a")] += 1
            s2count[ord(s2[i]) - ord("a")] += 1

        matches = 0
        for i in range(26):
            if s1count[i] == s2count[i]:
                matches += 1    # matches = 22
        
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            index = ord(s2[r]) - ord("a")
            s2count[index] += 1
            if s1count[index] == s2count[index]:
                matches += 1
            elif s1count[index] + 1 == s2count[index]:
                matches -= 1
            
            indx = ord(s2[l]) - ord("a")
            s2count[indx] -= 1
            if s1count[indx] == s2count[indx]:
                matches += 1
            elif s1count[indx] - 1 == s2count[indx]:
                matches -= 1
            l += 1
        return matches == 26


        