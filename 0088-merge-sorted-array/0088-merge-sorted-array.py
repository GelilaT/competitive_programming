class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
           #i=j=0
          # while j <= m+n:
           #     if nums1[i]==nums2[j]:
            #        nums1.insert(i+1,nums2[j])
             #       i+=2
              #      j+=1
               # if nums1[i]>nums2[j]:
            #        num1.insert(i-1,nums2[j])
             #       j+=1
              #  if nums1[i]<nums2[j]:
               #     i+=1
           #return nums1
        i=0
        for i in range(n):
            nums1[m]+=nums2[i]
            i+=1
            m+=1
        nums1.sort()
        return nums1