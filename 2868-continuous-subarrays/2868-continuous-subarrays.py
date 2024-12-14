class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        
        n = len(nums)
        left = 0
        my_dict = defaultdict(int)
        ans = 0
        for right in range(n):
            my_dict[nums[right]] += 1
            
            while max(my_dict.keys()) - min(my_dict.keys()) > 2:
                my_dict[nums[left]] -= 1

                if my_dict[nums[left]] == 0:
                    del my_dict[nums[left]]
                
                left += 1

            ans += right - left + 1

        return ans



