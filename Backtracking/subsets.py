class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        def combine(path, idx):
           if idx == len(nums) :
               return
           path.append(nums[idx])
           for i in range(idx + 1,len(nums)):
               combine(path,i)
               path.pop()
           subsets.append(path.copy())
           
    
        for i in range(len(nums)):
            combine([],i)
        return subsets
                
