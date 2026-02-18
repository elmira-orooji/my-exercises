text = input()

Vowels = ['a' , 'u', 'e', 'i', 'o']

total = 1

for ch in text:
    if ch in Vowels:
        total = total * 2
   

print(total)

