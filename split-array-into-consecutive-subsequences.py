class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        m = len(nums)
        n = m // 3
        my_dict = {}
        for i in range(m):
            # print(my_dict)

            if nums[i] - 1 in my_dict.keys() and nums[i] not in my_dict.keys():
                length = heappop(my_dict[nums[i] - 1]) + 1
                if not my_dict[nums[i] - 1]:
                    del my_dict[nums[i] - 1] 
                my_dict[nums[i]] = []
                heappush(my_dict[nums[i]], length)
            elif nums[i] - 1 in my_dict.keys() and nums[i] in my_dict.keys():
                length = heappop(my_dict[nums[i] - 1]) + 1
                if not my_dict[nums[i] - 1]:
                    del my_dict[nums[i] - 1] 
                heappush(my_dict[nums[i]], length)
            elif nums[i] - 1 not in my_dict.keys() and nums[i] not in my_dict.keys(): 
                my_dict[nums[i]] = []
                heappush(my_dict[nums[i]], 1)
            elif nums[i] - 1 not in my_dict.keys() and nums[i] in my_dict.keys(): 
                heappush(my_dict[nums[i]], 1)
           
        for val in my_dict.values():
            for i in range(len(val)):
                if val[i] < 3:
                    return False
        return True