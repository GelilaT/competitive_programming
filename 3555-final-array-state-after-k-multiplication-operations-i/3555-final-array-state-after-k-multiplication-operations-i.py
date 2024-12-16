class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        
        my_dict = defaultdict(list)
        heap = []
        n = len(nums)
        for i in range(n - 1, -1, -1):
            heappush(heap, (nums[i], i))

        while k:
            cur, idx = heappop(heap)
            cur *= multiplier
            heappush(heap, (cur, idx))
            nums[idx] *= multiplier
            k -= 1

        return nums


        

        