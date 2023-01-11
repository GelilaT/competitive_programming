class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        divided=num//3
        ans=[]
        for i in range(divided-1,divided+2):
            ans.append(i)
        if sum(ans) == num:
            return ans
        else:
            return []
