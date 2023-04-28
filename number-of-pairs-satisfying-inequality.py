class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        n = len(nums1)
        new = [0] * n
        count = 0
        for i in range(n):
            new[i] = nums1[i] - nums2[i]

        def mergeSort(left, right, arr):
            if left == right:
                return [arr[left]]
            mid = left + (right - left) // 2
            left_half = mergeSort(left, mid, arr)
            right_half = mergeSort(mid + 1, right, arr)
            return merge(left_half, right_half)

        def merge(left_half, right_half):
            nonlocal count
            merged = []
            l = r = right = 0
            for left in range(len(left_half)):
                while right < len(right_half) and left_half[left] > right_half[right] + diff:
                    right += 1
                count += (len(right_half) - right)

            while l < len(left_half) and r < len(right_half):
                if left_half[l] <= right_half[r]:
                    merged.append(left_half[l])
                    l += 1
                else:
                    merged.append(right_half[r])
                    r += 1
            merged.extend(left_half[l:])
            merged.extend(right_half[r:])
            return merged
        mergeSort(0,n - 1,new)
        return count