class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        b_count = 0
        ans = inf
        for i in range(len(blocks)):
            if i - k >= 0 and blocks[i - k] == 'B': 
                b_count -= 1
            
            if blocks[i] == 'B':
                b_count += 1            
            
            ans = min(ans, k - b_count)
        
        return ans