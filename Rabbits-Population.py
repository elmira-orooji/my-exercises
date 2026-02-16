P , L = map(int, input().split())
Y = int(input())

count = 0

while count < Y:
   P = ( P * 2 ) - L
   count += 1

print(P)

