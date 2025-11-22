class Solution:
    def compress(self, chars: List[str]) -> int:
        ans = 0
        l = 0
        while l < len(chars):
            temp1 = chars[l]
            temp = 1
            while l + 1 < len(chars) and chars[l] == chars[l+1]:
                temp += 1
                l += 1
            chars[ans] = temp1
            ans += 1  
            if temp > 1:
                temp2 = str(temp)
                for i in range(len(temp2)):
                    chars[ans] = temp2[i]
                    ans += 1
            l += 1
            
        return ans
            
