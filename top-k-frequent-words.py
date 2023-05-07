class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        heap = []
        for word in count:
            heappush(heap, (-count[word], word))
        ans = []
        print(heap)
        for i in range(k):
                ans.append(heappop(heap)[1])
        return ans