class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:

        n = len(arr)
        for i in range(n - 2, -1, -1):
            to_be_swapped = -inf
            index = None
            for j in range(i + 1, n):
                if arr[j] < arr[i]:
                    temp = to_be_swapped
                    to_be_swapped = max(to_be_swapped, arr[j])
                    if temp != to_be_swapped or index == None:
                        index = j
            
            # if arr[i] > arr[index]:
            if index != None:
                arr[i], arr[index] = arr[index], arr[i]
                break
        return arr



























        # nums = defaultdict(list)
        # for i in range(len(arr)):
        #     nums[arr[i]].append(i)

        # new = list(set(sorted(arr)))
        # if len(new) > 2:
        #     first = nums[new[-1]][0]
        #     second = nums[new[-2]][0] 
        #     third = nums[new[-3]][0]
        #     if first != 0 and first < second:
        #         arr[first], arr[second] = arr[second], arr[first]
        #     elif first == 0:
        #         arr[second], arr[third] = arr[third], arr[second]
        # else:
        #     if len(new) == 2:
        #         first = nums[new[-1]][0]
        #         second = nums[new[-2]][0]
        #         i = len(nums[new[-1]])
        #         j = len(nums[new[-2]])
        #         while i >= 0 and j >= 0:
        #             if nums[new[-1]][i] < nums[new[-2]][j]: 
        #                 arr[nums[new[-1]][i]], arr[nums[new[-2]][j]] = arr[nums[new[-2]][j]], arr[nums[new[-1]][i]]
        #                 break
        #             else:
        #                 i -= 1
        #                 j -= 1
    
        # return arr



























        # if len(new) > 2:
        #     if nums[new[-1][0]] != 0 and nums[new[-1][0]] < nums[new[-2][0]]:
        #         arr[nums[new[-1][0]]], arr[nums[new[-2][0]]] = arr[nums[new[-2][0]]], arr[nums[new[-1][0]]]
        #     elif nums[new[-1]] == 0:
        #         arr[nums[new[-2]]], arr[nums[new[-3]]] = arr[nums[new[-3]]], arr[nums[new[-2]]]
        # else:
        #     if len(new) == 2 and nums[new[-1]] < nums[new[-2]]:
        #         arr[nums[new[-1]]], arr[nums[new[-2]]] = arr[nums[new[-2]]], arr[nums[new[-1]]]
        
        # return arr
        
























        # if nums[-2][0] == arr[0] or nums[-1][0] == arr[0]:
        #     return arr
        # else:
        #     first = nums[-1][1]
        #     second = nums[-2][1]
        #     if arr[0] > arr[second]:
        #         arr[0], arr[second] = arr[second], arr[0]
        #     else:
        #         arr[first], arr[second] = arr[second], arr[first]
        #     return arr