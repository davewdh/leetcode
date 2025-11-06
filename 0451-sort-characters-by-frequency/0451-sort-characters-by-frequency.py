class Solution:
    def frequencySort(self, s: str) -> str:
        m = Counter(s)
        ans = ""
        for k, v in sorted(m.items(), key=lambda item: item[1], reverse=True):
            ans += (k * v)

        return ans