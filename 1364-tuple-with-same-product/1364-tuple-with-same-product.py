class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:

        n = len(nums)
        res = []
        for i in range(n - 1):
            for j in range(i + 1, n):
                res.append(nums[i] * nums[j])

        count = Counter(res)
        ans = 0
        for key, val in count.items():
            if val >= 2:
                cur = math.perm(val, 2)
                ans += (cur * 4) 

        return ans
        

        