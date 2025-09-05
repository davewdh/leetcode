class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        ans = []
        z = list(zip(heights, names))
        z.sort(reverse=True)
        h, n = zip(*z)
        return n

        