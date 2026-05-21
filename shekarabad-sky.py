n, m = map(int, input().split())

counter = 0

sumation = 0

user_list = []

while counter < n:
    user_input = input()
    user_list.append(user_input)
    counter += 1

for char in user_list:
    for i in char:
        if i == "*":
            sumation += 1
        else:
            continue
    
print(sumation)