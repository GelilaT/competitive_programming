row=len(grid)
col=len(grid[0])
transpose=[[0]*row for i in range(col)]
count=0
row_dict=defaultdict(list)
col_dict=defaultdict(list)
for i in range(row):
    for j in range(col):
        transpose[i][j]+=grid[j][i]
for index in range(row):
    row_dict[index].append(grid[index])
    col_dict[index].append(transpose[index])
for i in range(row):
    for j in range(row):
        if row_dict[i]==col_dict[j]:
            count+=1
return count
