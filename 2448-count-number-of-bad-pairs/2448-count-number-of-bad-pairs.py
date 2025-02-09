class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        
        diff = []
        n = len(nums)
        for i in range(len(nums)):
            diff.append(nums[i] - i)

        freq = Counter(diff)
        total_pairs = comb(n, 2)

        same_pairs = sum(comb(count, 2) for count in freq.values() if count > 1)

        return total_pairs - same_pairs