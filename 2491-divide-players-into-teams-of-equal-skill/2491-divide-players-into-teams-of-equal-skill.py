class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n = len(skill)
        s = skill[0] + skill[n-1]
        temp = [skill[0], skill[n-1]]
        ans = 0
        l, r = 1 , n-2
        while l <= r:
            if s != skill[l] + skill[r]:
                return -1
            else:
                temp.append(skill[l])
                temp.append(skill[r])
            l += 1
            r -= 1
        
        for i in range(0, n, 2):
            ans += (temp[i] * temp[i+1])

        return ans