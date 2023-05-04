t =int(input())
for _ in range(t):
    n = int(input())
    permutation = list(map(int, input().split()))
    count = [0]
    def mergeSort(arr, count):
        if len(arr) == 1:
            return arr
        mid = len(arr) // 2
        left_half = mergeSort(arr[ :mid], count)
        right_half = mergeSort(arr[mid: ], count)
        return merge(left_half, right_half, count)

    def merge(left_half, right_half, count):
        
        if left_half[0] < right_half[0]:
            left_half.extend(right_half)
            return left_half
        else:
            count[0] += 1
            right_half.extend(left_half)
            return right_half
    
    ans = mergeSort(permutation, count)
    if ans == sorted(permutation):
        print(count[0])
    else:
        print(-1)
