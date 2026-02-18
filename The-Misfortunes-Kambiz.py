s = input().strip()
n = len(s)

def valid(part):
   
    if len(part) == 0:
        return False
    
    if len(part) > 1 and part[0] == '0':
        return False
   
    if 0 <= int(part) <= 255:
        return True
    return False

for i in range(1, 4):
    for j in range(1, 4):
        for k in range(1, 4):
            if i + j + k >= n:
                continue
            l = n - (i + j + k)
            if l < 1 or l > 3:
                continue

            p1 = s[:i]
            p2 = s[i:i+j]
            p3 = s[i+j:i+j+k]
            p4 = s[i+j+k:]

            if valid(p1) and valid(p2) and valid(p3) and valid(p4):
                print(f"{p1}.{p2}.{p3}.{p4}")
