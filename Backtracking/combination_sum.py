class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        subsets = []
        def combine(path, idx, total):
           if idx == len(candidates):
               return
           if total > target:
               return
           if total == target:
               subsets.append(path.copy())
               return subsets
           path.append(candidates[idx])
           combine(path,idx,total + candidates[idx])
           path.pop()
           combine(path,idx+1,total)
        combine([],0,0)
        return subsets
      

         
                
