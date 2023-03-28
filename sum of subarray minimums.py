class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        sub_min = 0
        arr.append(-inf)
        for i in range(len(arr)):
            while stack and arr[stack[-1]] > arr[i]:
                index = stack.pop()
                if stack:
                    sub_min += arr[index] * ((i - index) * (index - stack[-1]))
                else:
                    sub_min += arr[index] * ((index + 1) * (i - index))
            stack.append(i)
        return sub_min % (10**9 + 7)
