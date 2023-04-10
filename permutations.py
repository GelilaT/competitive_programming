class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        def permutations(path, visited):

            if len(path) == n:
                ans.append(path.copy())
                return

            else:
                for i in range(n):
                    if nums[i] not in visited:
                        path.append(nums[i])
                        visited.add(nums[i])
                        permutations(path, visited)
                        path.pop()
                        visited.remove(nums[i])
        
        permutations([],set())
        return ans
