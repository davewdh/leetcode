class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        def helper(k):
            l = 0
            aMap = {}
            ans = 0
            count = 0

            for r in range(len(word)):
                if word[r] in "aeiou":
                    if aMap.get(word[r]):
                        aMap[word[r]] += 1
                    else:
                        aMap[word[r]] = 1
                else:
                    count += 1

                while len(aMap) == 5 and count >= k:
                    ans += len(word) - r
                    if word[l] in "aeiou":
                        aMap[word[l]] -= 1
                        if aMap[word[l]] == 0:
                            aMap.pop(word[l])
                    else:
                        count -= 1
                    l += 1
            return ans

        return helper(k) - helper(k+1)