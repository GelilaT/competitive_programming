class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count=collections.Counter(nums)
        goodpairs=0
        for i in count.values(): 
            pairs=(i*(i-1))//2
            goodpairs+=pairs
        return goodpairs   
