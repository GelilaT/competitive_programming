class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        dic={}
        count=0
        for number in nums:
            dic[number]=True
        for key in dic.keys():
            if dic.get(key+diff) and dic.get(key+(2*diff)):
                count+=1
        return count