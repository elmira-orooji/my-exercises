n = int(input())


for i in list(range(1 , n + 1)):
    for j in list(range(1 , n + 1)):
        print( i * j , end=' ')
    if j == n:
        print("\t")
        
