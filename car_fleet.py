class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
       stack = []
       for i in range(len(position)):
           time = (target - position[i]) / speed[i]
           stack.append([position[i],time])

       cur = None
       count = 0
       stack.sort(reverse = True)
       for position,time in stack:
           if not cur:
               cur = time
               count += 1
           elif cur >= time:
               continue
           else:
               cur = time
               count += 1
       return count
