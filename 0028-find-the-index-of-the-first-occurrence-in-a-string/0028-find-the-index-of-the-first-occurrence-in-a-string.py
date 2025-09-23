class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                count = 1
                for j in range(1, len(needle)):
                    if haystack[i+j] != needle[j]:
                        break
                    count += 1
                if count == len(needle):
                    return i
        return -1
                
        
