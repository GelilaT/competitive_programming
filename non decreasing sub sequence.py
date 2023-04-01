class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        path = []
        def sequence(idx):
            nonlocal ans
            if idx == len(nums):
                return
            temp = path[-1] if path else None
            if temp == None or path[-1] <= nums[idx]:
                path.append(nums[idx])
                if len(path) >= 2:
                    ans.add(tuple(path.copy()))
                sequence(idx + 1)
                path.pop()
            sequence(idx + 1)
        
            return ans
        return sequence(0)


            
