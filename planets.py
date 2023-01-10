n=int(input())
for i in range(n):
    nums=list(map(int, input().split()))
    orbit=nums[0]
    cost=nums[1]
    planets=list(map(int,input().split()))
    my_dict={} 
    for index in range(orbit):
        if planets[index] not in my_dict:
            my_dict[planets[index]]=1
        else:
            my_dict[planets[index]]+=1
    total_cost=0
    for val in my_dict.keys():
        if my_dict[val] != 1:
            if cost > my_dict[val]:
                total_cost+=my_dict[val]
            else:
                total_cost+=cost
        elif my_dict[val] == 1:
            total_cost+=1
    print(total_cost)

