class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        ans = 0
        heap = []

        for i in range(len(nums)):
            heappush(heap, nums[i])

        while len(heap) >= 2 and heap[0] < k:
            ans += 1
            first = heappop(heap)
            second = heappop(heap)

            res = first * 2 + second

            heappush(heap, res)

        return ans