class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        prefix=0
        ans=0
        my_dict={}

        for num in nums:
            my_dict[prefix] = 1 + my_dict.get(prefix, 0)
            prefix += num
            if prefix - goal in my_dict:            
                ans += my_dict[prefix - goal]      

        return ans
