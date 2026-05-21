n = int(input())
k = int(input())
p = int(input())
q = int(input())

shekarestan = n - k
namakestan = p - q

if shekarestan < namakestan:
    print("Namakestan")
elif shekarestan > namakestan:
    print("Shekarestan")
else:
    print("Equal")