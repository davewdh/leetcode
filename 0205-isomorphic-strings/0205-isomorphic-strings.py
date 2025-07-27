class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def helper(s, t):
            dic = {}
            for i in range(len(s)):
                if s[i] in dic:
                    if dic[s[i]] != t[i]:
                        return False
                dic[s[i]] = t[i]
            return True
        return helper(s, t) and helper(t, s)