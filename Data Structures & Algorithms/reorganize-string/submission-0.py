class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxHeap = [[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(maxHeap)

        prev = None
        res = ""
        while maxHeap:            
            cnt, char = heapq.heappop(maxHeap)

            if not prev or prev != char:
                res += char
                prev = char
                if cnt + 1 < 0:
                    heapq.heappush(maxHeap, [cnt + 1, char])

            else:
                if not maxHeap:
                    return ""
                cnt1, char1 = heapq.heappop(maxHeap)
                res += char1
                prev = char1

                heapq.heappush(maxHeap, [cnt, char])
                if cnt1 + 1 < 0:
                    heapq.heappush(maxHeap, [cnt1 + 1, char1])


        return res