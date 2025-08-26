class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ans = []
        m = {}
        for c in words[0]:
            if m.get(c):
                m[c] += 1
            else:
                m[c] = 1

        for i in range(1, len(words)):
            temp = {}
            m1 = {}    
            for c in words[i]:
                if m1.get(c):
                    m1[c] += 1
                else:
                    m1[c] = 1
            for k, v in m.items():
                if k in m1:
                    if m.get(k) < m1.get(k):
                        temp[k] = v
                    else:
                        temp[k] = m1.get(k)
            m = temp

        for k, v in m.items():
            for i in range(v):
                ans.append(k)

        return ans