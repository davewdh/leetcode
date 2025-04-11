class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []

        for a in asteroids:
            while s and a < 0 < s[-1]:
                if s[-1] > -a:
                    a = 0
                elif s[-1] < -a:
                    s.pop()
                else:
                    s.pop()
                    a = 0
            if a:
                s.append(a)
        return s
