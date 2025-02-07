class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        
        count = 0
        colors = defaultdict(int)
        balls = {}
        ans = []
        for ball, color in queries:
            if ball in balls:
                prev = balls[ball]
                colors[prev] -= 1
                if colors[prev] == 0:
                    del colors[prev]

                balls[ball] = color
                
            else:
                balls[ball] = color
            
            colors[color] += 1
            ans.append(len(colors))

        return ans