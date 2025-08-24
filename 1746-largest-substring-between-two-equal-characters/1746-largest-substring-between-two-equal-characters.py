class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        m = {}
        ans = 0
        for i in range(len(s)):
            if m.get(s[i]):
                if len(m.get(s[i])) > 1:
                    m[s[i]][-1] = i
                else:
                    m[s[i]].append(i)
            else:
                m[s[i]] = [i]

        for v in m.values():
            ans = max(ans, v[-1] - v[0] - 1)
        if len(s) == len(m):
            return -1
        return ans