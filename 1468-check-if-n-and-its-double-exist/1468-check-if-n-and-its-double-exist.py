class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        nums = set()
        
        for i in range(len(arr)):
            num1 = arr[i] * 2
            num2 = arr[i] / 2
            if num1 in nums or num2 in nums:
                return True

            else:
                nums.add(arr[i])

        return False
        