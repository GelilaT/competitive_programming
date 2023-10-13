# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        
        n = mountain_arr.length()
        def get_max(n):

            high = n - 1
            low = 0
            while low <= high:
                mid = low + (high - low) // 2
                middle = mountain_arr.get(mid)
                next_ele = mountain_arr.get(mid + 1)

                if middle < next_ele:
                    low = mid + 1

                elif middle > next_ele:
                    high = mid - 1

            return low

        def right(low, high):

            while low <= high:
                mid = low + (high - low) // 2
                middle = mountain_arr.get(mid)

                if target == middle:
                    return mid

                elif middle < target:
                    high = mid - 1

                else:
                    low = mid + 1

            return -1

        def left(low, high):

            while low <= high:
                mid = low + (high - low) // 2
                middle = mountain_arr.get(mid)

                if target == middle:
                    return mid

                elif middle < target:
                    low = mid + 1

                else:
                    high = mid - 1

            return -1

        idx = get_max(n)
        
        res1 = left(0, idx)
        if res1 != -1:
            return res1

        res2 = right(idx + 1, n - 1)
        return res2