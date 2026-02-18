x1 , x2 = map(int, input().split())

if x1 == x2:
    print("Saal Noo Mobarak!")

elif x1 == 0 and x2 == 2:
    print("RR")

elif x1 == 2 and x2 == 0:
    print("LL")

elif x1 == 1 and x2 == 2:
    print("R")

elif x1 == 2 and x2 == 1:
    print("L")

elif x1 == 1 and x2 == 0:
    print("L")

elif x1 == 0 and x2 == 1:
    print("R")    