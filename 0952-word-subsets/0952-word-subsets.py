class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        m = {}
        ans = []
        for s in words2:
            c = Counter(s)
            for char in s:
                if m.get(char):
                    m[char] = max(m.get(char), c[char])
                else:
                    m[char] = c[char]

        for s in words1:
            s1 = "".join(sorted(s))
            temp = True
            for k, v in m.items():
                if k * v not in s1:
                    temp = False
                    break
            if temp:
                ans.append(s)
        
        return ans
                
        
