class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1 = ""
        r1 = len(s) - 1
        while r1 >= 0:
            if s[r1] != "#":
                s1 += s[r1]
                r1 -= 1
            else:
                skip = 0
                while r1 >= 0 and s[r1] == "#":
                    r1 -= 1
                    skip += 1
                
                while r1 >= 0 and skip:
                    if s[r1] == "#":
                        skip += 1
                    else:
                        skip -= 1
                    r1 -= 1
            
        s2 = ""
        r2 = len(t) - 1
        while r2 >= 0:
            if t[r2] != "#":
                s2 += t[r2]
                r2 -= 1
            else:
                skip = 0
                while r2 >= 0 and t[r2] == "#":
                    r2 -= 1
                    skip += 1

                while r2 >= 0 and skip:
                    if t[r2] == "#":
                        skip += 1
                    else:
                        skip -= 1
                    r2 -= 1
            
        return s1 == s2