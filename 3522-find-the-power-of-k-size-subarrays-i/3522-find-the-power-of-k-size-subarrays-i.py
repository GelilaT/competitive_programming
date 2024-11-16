class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = []
        for i in range(n - k + 1):
            for j in range(i, i + k - 1):
                if nums[j + 1] < nums[j] or nums[j + 1] != nums[j] + 1:
                    ans.append(-1)
                    break
            
            else:
                ans.append(nums[i + k - 1])

        return ans
