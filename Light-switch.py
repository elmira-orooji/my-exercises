n = int(input())

counter = 0
change_state = 0
state_list = []

while counter < n:
    light_state = int(input())
    state_list.append(light_state)
    counter += 1

for i in range(len(state_list) - 1):
    if state_list[i] == 0 and state_list[i + 1] == 1:
        change_state += 1
    elif state_list[i] == 1 and state_list[i + 1] == 0:
        change_state += 1

print(change_state)






