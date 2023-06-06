class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
      cur_time = 1
      heap = []
      n = len(tasks)
      result = []
      time_heap = []
      for i in range(n):
         heappush(heap,tasks[i] + [i])
      
      while len(result) < len(tasks):
         while len(heap) > 0 and heap[0][0] <= cur_time:
            cur_task = heappop(heap)
            cur_task = (cur_task[1], cur_task[2], cur_task[0])
            heappush(time_heap, cur_task)
         
         if len(time_heap) == 0 and len(heap) > 0:
            cur_time = heap[0][0]
         
         else:
            task = heappop(time_heap)
            cur_time += task[0]
            result.append(task[1])

      return result