class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower_str = s.lower()
        cleaned_str = re.sub(r'[^a-z0-9]', '', lower_str)
        start_point = 0
        end_point = len(cleaned_str) - 1
        while start_point < end_point:
            if cleaned_str[start_point] != cleaned_str[end_point]:
                return False
            start_point += 1
            end_point -= 1
        return True