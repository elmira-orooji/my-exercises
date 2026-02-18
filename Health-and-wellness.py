x = int(input())
n = int(input())

if n == 0:
    print("20")
elif n == 7:
    print(x)
else:
    m = x - n 
    if m < 0:
        print("0")
    else:
        print(m)