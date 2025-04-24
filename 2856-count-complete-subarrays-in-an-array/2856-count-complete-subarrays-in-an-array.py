class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        
        k = len(set(nums))
        freq = {}
        left = 0
        result = 0

        for right in range(len(nums)):

            freq[nums[right]] = freq.get(nums[right], 0) + 1
            while len(freq) == k:
                result += len(nums) - right
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]

                left += 1

        return result
