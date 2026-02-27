n = int(input())

count = 0

CAPS = False

name = ""

while count < n:
    user_input = input()
    count += 1

    if user_input == 'CAPS':
        CAPS = True
        while CAPS == True:
            user = input() 
            name = name + user.upper()
            count += 1 
            if user_input == 'CAPS':
                break
        
        

    else:
        name = name + user_input  
    

print(name)


        

