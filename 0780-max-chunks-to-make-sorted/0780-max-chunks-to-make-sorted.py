class Solution:
    def maxChunksToSorted(self, arr):
        if not arr:
            return 0

        chunk = 0
        max_val = 0

        for i in range(len(arr)):
            max_val = max(max_val, arr[i])
            if max_val == i:
                chunk += 1

        return chunk