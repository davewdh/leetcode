class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        arr = [0] * len(words)
        for i in range(len(words)):
            if words[i][0] in "aeiou" and words[i][-1] in "aeiou":
                arr[i] = 1
        prefix = [0] * (len(words) + 1)
        for i in range(len(words)):
            prefix[i+1] = prefix[i] + arr[i]
        ans = []
        for q in queries:
            temp = prefix[q[-1]+1] - prefix[q[0]]
            ans.append(temp)
        return ans
        