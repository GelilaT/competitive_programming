class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        heap = []
        for word in count:
            heappush(heap, (-count[word], word))
        ans = []
        print(heap)
        for i in range(k):
            if ans and count[ans[-1]] == count[heap[0][1]] and ans[-1] > heap[0][1]:
                ans.append(heappop(heap)[1])
                ans[-2], ans[-1] = ans[-1], ans[-2]
            else:
                ans.append(heappop(heap)[1])

        return ans