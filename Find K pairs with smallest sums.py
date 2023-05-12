class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        heappush(heap, [nums1[0]+ nums2[0], 0, 0])
        visited = set((0, 0))
        n, m = len(nums1), len(nums2)
        ans = []
        while heap and len(ans) < k: 

            summ, index1, index2 = heappop(heap)
            ans.append([nums1[index1],nums2[index2]])

            if (index1 + 1, index2) not in visited and index1 + 1 < n:
                heappush(heap, [nums1[index1 + 1] + nums2[index2], index1 + 1, index2])
                visited.add((index1 + 1, index2))

            if (index1, index2 + 1) not in visited and index2 + 1 < m:
                heappush(heap, [nums1[index1] + nums2[index2 + 1], index1, index2 + 1])
                visited.add((index1, index2 + 1))

        return ans 
