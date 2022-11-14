class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix=0
        prefixsum=[0]
        for j in range(len(gain)):
             prefix+=gain[j]
             prefixsum.append(prefix)
        return max(prefixsum)