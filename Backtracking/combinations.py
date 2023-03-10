class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        ans = []
        def search(temp , idx):
            if len(temp) == k:
                ans.append(temp)
                return
            if idx == n + 1:
                return 
       
            search(temp, idx + 1)
            search(temp+[idx], idx + 1) 

        search([],1)
        return ans
