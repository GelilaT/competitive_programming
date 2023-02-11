class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        count={}
        
        for num in nums:
          if num not in count:
              count[num]=1
        for num in nums:
            in_str=str(num)
            reverse=int(in_str[len(in_str)::-1])
            if reverse not in count:
                count[reverse]=1
        
        
        return len(count)
