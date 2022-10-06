class Solution(object):
    def minSetSize(self, arr):
        from collections import Counter
        count=Counter(arr)
        half=len(arr)//2
        result=0
        for k,v in sorted(count.items(), key=lambda x:-x[1]):
            if half>0:
                result += 1
                half -= v
            else:
                break
        return result