class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        if s == t:
            return True
        if len("".join(set(s))) != len("".join(set(t))):
            return False
        dic = {}
        for i in range(len(s)):
            if s[i] in dic:
                if dic[s[i]] != t[i]:
                    return False
            dic[s[i]] = t[i]
        return True
        