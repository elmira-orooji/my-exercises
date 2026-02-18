n = int(input())
my_list = list(map(int, input().split()))

for i in my_list:
    if i == 1:
        print("*")
    elif i == 2:
        print("**")
    elif i == 3:
        print("***")
    else:
        print("*")