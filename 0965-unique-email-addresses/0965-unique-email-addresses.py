class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        ans = set()
        for email in emails:
            temp = ""
            for i, c in enumerate(email):
                if c == "@":
                    temp += email[i:]
                    break
                if c == "+":
                    temp += email[email.index("@"):]
                    break
                if c != ".":
                    temp += c
            ans.add(temp)
        return len(ans)