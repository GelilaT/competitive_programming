class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diff = []
        for i in range(len(costs)):
            diff.append((i, costs[i][0] - costs[i][1]))

        min_cost = 0
        n = len(costs) // 2
        diff.sort(key=lambda x:x[1])
        for i in range(n):
            min_cost += costs[diff[i][0]][0] 
        
        for i in range(n, 2 * n):
            min_cost += costs[diff[i][0]][1]
        
        return min_cost