class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        
        digit = defaultdict(list)
        for num in nums:
            total = 0
            temp = num
            while num > 0:
                total += num % 10
                num //= 10

            heappush(digit[total], -temp)

  
        ans = -1
        for key, val in digit.items():
            if len(val) < 2:
                continue

            ans = max(ans, -heappop(val) - heappop(val))

        return ans