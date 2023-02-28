class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        prefix=[0] * k
        prefix[0] = 1
        running=0
        sub_arrays=0
        for num in nums:
            running=(running + num) % k
            sub_arrays += prefix[running]
            prefix[running] += 1

        return sub_arrays
