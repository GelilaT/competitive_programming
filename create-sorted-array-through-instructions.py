from sortedcontainers import SortedList

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        nums = SortedList()
        cost = 0
        for i in range(len(instructions)):

            left = nums.bisect_left(instructions[i])
            right = len(nums) - nums.bisect_right(instructions[i])
            cost += min(left, right)
            nums.add(instructions[i])
        
        
        return cost % ((10 ** 9) + 7)