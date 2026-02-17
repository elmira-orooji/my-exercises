a , b = map(int, input().split())

if a != 0 :
    print("unique")
elif a == 0 and b == 0:
    print("infinite")
else:
    print("invalid")