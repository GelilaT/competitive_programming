class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        
        ans = 0
        heaters = sorted(heaters)
        for house in houses:

            mini = inf
            low = 0
            high = len(heaters) - 1

            while low <= high:
                mid = low + (high - low) // 2

                if heaters[mid] > house:
                    high = mid - 1
                
                else:
                    low = mid + 1

                mini = min(mini, abs(heaters[mid] - house))
            
            ans = max(ans, mini)

        return ans
    
        # ans=0
        # heaters = sorted(heaters)
        # for i in range(len(houses)):
        #     minimum = inf
        #     low = 0
        #     high = len(heaters) - 1
        #     while low <= high:
        #         mid = low + (high - low)//2
        #         if heaters[mid] > houses[i]:
        #             high = mid - 1
                
        #         else:
        #             low = mid + 1
        #         minimum = min(minimum, abs(heaters[mid] - houses[i]))
        #     ans = max(ans, minimum)
        # return ans