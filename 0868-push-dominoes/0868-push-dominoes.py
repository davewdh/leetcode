class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = "L" + dominoes + "R"
        ans = ""
        i = 0

        for j in range(1, len(dominoes)):
            if dominoes[j] == ".":
                continue
            middle = j - i - 1
            if i:
                ans += dominoes[i]
            if dominoes[i] == dominoes[j]:
                ans += (dominoes[i] * middle)
            elif dominoes[i] == "L" and dominoes[j] == "R":
                ans += ("." * middle)
            else:
                ans += (dominoes[i] * int(middle/2)) + ("." * (middle%2)) + (dominoes[j] * int(middle/2))
            i = j
        return ans



