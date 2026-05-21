n, k = map(int, input().split())

counter = 0
result = []

while counter < n:
    a , b , x = map(int, input().split())  
    if k == x:
        result.append(a)
        counter += 1
    elif x > k:
        result.append(a)
        counter += 1
    else:
        z = k - x
        c = z * b
        new_a = a + c
        result.append(new_a)
        counter += 1

min_num = min(result)
final_result = result.index(min_num) + 1
print(final_result)
    