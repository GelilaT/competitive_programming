class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
       heap = []
       index = cur = 0
       for i in range(1, len(heights)):
            diff = heights[i] - heights[i - 1] if heights[i] > heights[i - 1] else 0
            cur = i
            # print(diff)
            if ladders == 0 and bricks == 0 and diff != 0:
                    return 0
            elif ladders == 0 and bricks == 0 and diff == 0:
                return cur
            elif not heap:
                heappush(heap, diff)

            else:
                if len(heap) < ladders:
                    heappush(heap, diff)
                elif len(heap) == ladders and ladders != 0:
                        if heap[0] <= diff and bricks >= heap[0]:
                            heappush(heap, diff)
                            bricks -= heappop(heap)
                        elif heap[0] > diff and bricks >= diff:
                            bricks -= diff
                        else:
                            index = i
                            break
                elif ladders == 0:
                    if bricks > diff:
                        bricks -= diff
                    else:
                        index = i
                        break
                    
       if index:
            return index - 1
       else:
           return cur