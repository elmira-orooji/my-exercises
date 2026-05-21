n = int(input())

divisor = 1

total_divisor = 0

while total_divisor < n:

    if n % divisor == 0:
        total_divisor = total_divisor + divisor
        divisor += 1
    else:
        divisor += 1
        

if total_divisor == n:
    print("YES")

else:
    print("NO")