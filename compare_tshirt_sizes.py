n=int(input())
my_dict={"S":1,"M":2,"L":3}
for i in range(n):
    size=input().split(" ")
    size1=size[0]
    size2=size[1]
    if size1[-1] == size2[-1]:
        if size1[-1]=="L":
            if len(size1) < len(size2):
                print("<")
            elif len(size1) > len(size2):
                print(">")
            else:
                print("=")
        elif size1[-1]=="S":
            if len(size1) < len(size2):
                print(">")
            elif len(size1) > len(size2):
                print("<")
            else:
                print("=")
        else:
            print("=")
    elif size1[-1] != size2[-1]:
        if my_dict[size1[-1]] < my_dict[size2[-1]]:
            print("<")
        elif my_dict[size[0][-1]] > my_dict[size[1][-1]]:
            print(">")



    
