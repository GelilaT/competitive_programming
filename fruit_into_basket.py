class Solution:
    def totalFruit(self, fruit: List[int]) -> int:
            maxfruit=0
            count={}
            left=0
            for right in range(len(fruit)):
                count[fruit[right]] = 1 + count.get(fruit[right] , 0)
                while len(count) > 2:
                    count[fruit[left]] -= 1
                    if count[fruit[left]] == 0:
                        del count[fruit[left]]
                    left+=1

                maxfruit=max(maxfruit , right-left+1)
            return maxfruit
