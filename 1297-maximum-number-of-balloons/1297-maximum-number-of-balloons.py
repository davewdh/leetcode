class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        aMap = {}
        for c in text:
            if c in "balloon":
                if aMap.get(c):
                    aMap[c] += 1
                else:
                    aMap[c] = 1
        if len(set("balloon")) != len(set(aMap.keys())):
            return 0
        if aMap.get('l'):
            num_l = aMap.get('l')
            aMap['l'] = floor(num_l/2)
        if aMap.get('o'):
            num_o = aMap.get('o')
            aMap['o'] = floor(num_o/2)
        values = list(aMap.values())
        values.sort()
        return values[0]
        
