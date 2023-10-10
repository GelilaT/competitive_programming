class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        if sum(gas) < sum(cost):
            return -1

        i, j = 0, 1
        val = gas[i] - cost[i]
        while j < len(gas):

            if val < 0:
                val = gas[j] - cost[j]
                i = j

            else:
                val += gas[j] - cost[j]

            j += 1

        return i