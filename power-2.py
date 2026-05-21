n = int(input())

power = 0

while True:
    temp = 2 ** power
    if temp > n:
        print(temp)
        break
    else:
        power += 1
        continue






