class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        prefix = [0] * (len(words) + 1)
        pre = 0
        for i in range(len(words)):
            if words[i][0] in "aeiou" and words[i][-1] in "aeiou":
                pre += 1
            prefix[i+1] = pre
        ans = []
        for q in queries:
            ans.append(prefix[q[-1]+1] - prefix[q[0]])
        return ans
        