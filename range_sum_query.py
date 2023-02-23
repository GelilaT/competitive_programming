class NumArray:

    def __init__(self, nums: List[int]):
        
        self.nums=nums
        self.prefix=[0]
        self.pre_sum=0

        for num in nums:
            self.pre_sum+=num
            self.prefix.append(self.pre_sum)

    def sumRange(self, left: int, right: int) -> int:
       
       return self.prefix[right+1] - self.prefix[left]
       
