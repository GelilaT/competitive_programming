class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
            sums=0
            answer=[]
            for index in range(len(nums)):
                if nums[index]%2==0:
                    sums+=nums[index]
            for val,index in queries:
                if nums[index]%2==0:
                    sums-=nums[index]
                nums[index]+=val
                if nums[index]%2==0:
                    sums+=nums[index]
                answer.append(sums)
            return answer
