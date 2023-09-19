class Solution:
    def minSteps(self, x: int) -> int:

        memo = {}
        if x == 1:
            return 0

        def minOp(op, i, total):

            if total == x:
                return 0

            if total > x:
                return float('inf')

            if (op, i, total) not in memo:

                if op == 'P':
                    memo[(op, i, total)] = min(minOp('P', i, total + i), minOp('C', total, total)) + 1
                else:
                    memo[(op, i, total)] = minOp('P', i, total + i) + 1
            
            return memo[(op, i, total)]
        
        return minOp('C', 1, 1) + 1