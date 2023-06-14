class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        
        total = 0
        ans = 0
        for i in range(len(nums)):
            total += nums[i]
            ans = max(ans, (total + i) // (i + 1))
        return ans
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # heap = []
        # for i in range(len(nums) - 1):
        #     diff = nums[i] - nums[i + 1]
        #     if diff < 0:
        #         heappush(heap, (diff, i, i + 1))
        
        # print(heap)
        
        # while heap:

        #     diff, first, second = heappop(heap)
        #     nums[first] += 1
        #     nums[second] -= 1
        #     cur = nums[first] - nums[second]
        #     if cur < 0:
        #         heappush(heap, (cur, first, second))
        # return max(nums)