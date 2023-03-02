class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
       
        n=len(nums)
        prefix=0
        prefix_arr=[0] * (n+1)

        for i in range(n):
            prefix += nums[i]
            prefix_arr[i+1] = prefix

        ans = n+1
        min_arr= deque()
        for right in range(n+1):

            while min_arr and prefix_arr[min_arr[-1]] > prefix_arr[right] :
                min_arr.pop()

            while min_arr and prefix_arr[right] - prefix_arr[min_arr[0]] >= k:
                ans=min(ans , right - min_arr[0])
                min_arr.popleft()

            min_arr.append(right)
        if ans == n+1 :
            return -1
        return ans
       
