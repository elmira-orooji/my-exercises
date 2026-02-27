n = int(input())

lights =  list(map(int, input().split()))

off_or_on = list(map(int, input().split()))

indexes = [i for i, value in enumerate(off_or_on) if value == 1]

result = []

for j in indexes:
    result.append(lights[j])

final_result = sorted(result)
print(" ".join(map( str, final_result )))