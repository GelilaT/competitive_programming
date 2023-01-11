class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        from collections import defaultdict
        n=len(boxes)
        ans=[0]*n
        my_dict=defaultdict(list)
        for i in range(n):
            my_dict[boxes[i]].append(i)
        indexlist=my_dict["1"]
        for index in range(n):
            for i in range(len(indexlist)):
                ans[index]+=abs(indexlist[i]-index)
        return ans
