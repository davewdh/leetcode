class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0
        sortedChars = ''.join(sorted(chars))
    
        def goodStr(s):
            aMap = {}
            for c in s:
                if aMap.get(c):
                    aMap[c] += 1
                else:
                    aMap[c] = 1
            for k, v in aMap.items():
                temp = v * k
                if temp not in sortedChars:
                    return False
            return True


        for s in words:
            if goodStr(s):
                ans += len(s)
        return ans