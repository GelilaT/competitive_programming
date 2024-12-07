class Solution:
    def minimumSize(self, nums, maxOperations):
        low, high = 1, max(nums)
        ans = high

        while low <= high:
            mid = (low + high) // 2
            count = 0

            for n in nums:
                count += (n - 1) // mid
                if count > maxOperations:
                    break

            if count <= maxOperations:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans