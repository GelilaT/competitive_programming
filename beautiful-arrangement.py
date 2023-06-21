class Solution:
    def countArrangement(self, n: int) -> int:
        nums = [i for i in range(1, n + 1)]
        count = 0

        def backtrack(idx):
            nonlocal count
            if idx == n:
                count += 1
            
            for i in range(idx, n):

                nums[idx], nums[i] = nums[i], nums[idx]

                if nums[idx] % (idx + 1) == 0 or (idx + 1) % nums[idx] == 0:
                    backtrack(idx + 1)
                nums[idx], nums[i] = nums[i], nums[idx]
            
        backtrack(0)
        return count