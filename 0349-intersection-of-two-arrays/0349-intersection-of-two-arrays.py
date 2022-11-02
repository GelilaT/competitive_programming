class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
             dic={}
             result=[]
             for i in range(len(nums1)):
                dic[nums1[i]]=0
             for num in nums2:
                if num in dic:
                    if num not in result:
                      result.append(num)
             return result