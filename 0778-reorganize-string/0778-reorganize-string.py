class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s) # hashmap, eg. a: 3, b: 1
        maxHeap = [[-cnt, c] for c, cnt in counts.items()]
        heapq.heapify(maxHeap)

        prev = None
        ans = ""

        while maxHeap or prev:

            if not maxHeap and prev:
                return ""

            cnt, c = heapq.heappop(maxHeap)
            ans += c
            cnt += 1

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None

            if cnt < 0:
                prev = [cnt, c]

        return ans

            

