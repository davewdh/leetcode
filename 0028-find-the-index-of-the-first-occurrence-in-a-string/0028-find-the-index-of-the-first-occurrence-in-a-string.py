class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i] == needle[0]:
                count = 1
                for j in range(1, len(needle)):
                    if haystack[i+j] != needle[j]:
                        break
                    count += 1
                if count == len(needle):
                    return i
        return -1
                
        
