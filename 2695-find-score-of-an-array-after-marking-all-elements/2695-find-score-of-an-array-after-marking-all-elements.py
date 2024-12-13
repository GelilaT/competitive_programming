class Solution:
    def findScore(self, nums: List[int]) -> int:
        
        my_dict = defaultdict(list)
        for i in range(len(nums) - 1, -1, -1):
            my_dict[nums[i]].append(i)

        heap = []
        for num in nums:
            heappush(heap, num)

        score = 0
        while heap:
            
            cur = heappop(heap)
            idx = my_dict[cur].pop()
            if nums[idx] != 0:
                score += cur
                if idx + 1 < len(nums):
                    nums[idx + 1] = 0

                if idx - 1 >= 0:
                    nums[idx - 1] = 0

                nums[idx] = 0
            
        return score