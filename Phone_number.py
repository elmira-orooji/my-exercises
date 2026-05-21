n = int(input)

count = 0

phone_num = []

while count < n:
    s = (input)
    for i in s:
        if len(s) != 11:
            print("invalid")
        elif s[0] == '+' and s[1] == '9' and s[2] == '8' and len(s) == 11:
            print(s) 
        elif s[0] == '0' and s[1] == '9' and len(s) == 11:
            print()
    

