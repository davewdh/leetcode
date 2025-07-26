class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []
        n = len(words)
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if words[i] in words[j]:
                    if words[i] not in ans:
                        ans.append(words[i])

        return ans