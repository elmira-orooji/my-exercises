n = int(input())
temps = list(map(int, input().split()))

for t in temps:
    if t > 15:
        print("cooler")
    else:
        print("heater")

