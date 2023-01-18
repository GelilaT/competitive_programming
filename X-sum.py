n=int(input())
for j in range(n):
    matrix=[]
    m=list(map(int, input().split()))
    rows=m[0]
    cols=m[1]
    diagonal_dict={}
    reverse_dict={}
    for i in range(rows):
        r=list(map(int,input().split()))
        matrix.append(r)
        maximum=0
    for row in range(rows):
        for col in range(cols):
            sums=row+col
            if sums in reverse_dict:
                reverse_dict[sums]+=matrix[row][col]
            else:
                reverse_dict[sums]=matrix[row][col]
            diff=col-row
            if diff in diagonal_dict:
                diagonal_dict[diff]+=matrix[row][col]
            else:
                diagonal_dict[diff]=matrix[row][col]
    for row in range(rows):
        for col in range(cols):
            sums=row+col
            diff=col-row
            all_sum=reverse_dict[sums]+diagonal_dict[diff]-matrix[row][col]
            maximum=max(maximum, all_sum)
    print(maximum)
