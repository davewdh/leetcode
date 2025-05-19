class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        ans = ""
        maxHeap = []
        for count, char in [(-a, "a"), (-b, "b"), (-c, "c")]:
            if count < 0:
                heapq.heappush(maxHeap, (count, char))

        while maxHeap:
            count, char = heapq.heappop(maxHeap)
            if len(ans) > 1 and ans[-1] == ans[-2] == char:
                if not maxHeap:
                    break
                count2, char2 = heapq.heappop(maxHeap)
                ans += char2
                count2 += 1
                if count2 < 0:
                    heapq.heappush(maxHeap, (count2, char2))
            else:
                ans += char
                count += 1
            if count < 0:
                heapq.heappush(maxHeap, (count, char))

        return ans






