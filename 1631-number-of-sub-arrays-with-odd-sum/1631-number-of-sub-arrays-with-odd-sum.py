class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        mod = 10**9 + 7
        odd_cnt, even_cnt = 0, 1
        curr_sum, res = 0, 0
        
        for num in arr:
            curr_sum += num
            if curr_sum % 2 == 0:
                res += odd_cnt
                even_cnt += 1
            else:
                res += even_cnt
                odd_cnt += 1
                
        return res % mod
        