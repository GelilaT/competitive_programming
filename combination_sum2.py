class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        candidates.sort()
        def combination(path, target, idx):
            # if target < 0:
            #     return
            if target == 0:
                combinations.append(path.copy())
                return
            for i in range(idx ,len(candidates)):
                # path.append()
                if i - 1 >= idx and candidates[i] == candidates[i - 1]:
                    continue 
                if target - candidates[i] < 0:
                    return
                combination(path + [candidates[i]], target - candidates[i],i + 1)
                # path.pop()
        combination([],target,0)
        return combinations
