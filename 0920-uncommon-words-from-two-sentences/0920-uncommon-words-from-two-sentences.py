class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        arr = (s1 + " " + s2).split(" ")
        m = {}
        for i in range(len(arr)):
            if m.get(arr[i]):
                m[arr[i]] += 1
            else:
                m[arr[i]] = 1
        ans = []
        for k, v in m.items():
            if v == 1:
                ans.append(k)
        return ans
            