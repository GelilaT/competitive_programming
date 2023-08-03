class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:

        answer = 0
        degree = [0] * n

        def maxRequest(i, count):
            
            nonlocal answer
            if i == len(requests):
                for i in range(n):
                    if degree[i]:
                        return
            
                answer = max(answer, count)
                return
        
            degree[requests[i][0]] -= 1
            degree[requests[i][1]] += 1
            maxRequest(i + 1, count + 1)

            degree[requests[i][0]] += 1
            degree[requests[i][1]] -= 1
            maxRequest(i + 1, count)

        maxRequest(0, 0)
        
        return answer