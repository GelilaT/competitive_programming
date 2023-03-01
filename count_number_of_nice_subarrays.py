class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        nums=[ num % 2 for num in nums]
        prefixes=defaultdict(int)
        prefixes[0]=1

        sub_arrays=0
        running_sum=0
        for num in nums:
            running_sum += num
            sub_arrays += prefixes[running_sum - k]
            prefixes[running_sum] += 1
        
        return sub_arrays
