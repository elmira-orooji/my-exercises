key = input()
q = int(input())

count = 0

while count < q:
    guess = input()
    count += 1
    if len(guess) != len(key):
        print("Invalid Length")
    for i in guess:
        for j in key:
            if i == j and guess.index(i) == key.index(j):
                print("G",end='')
            elif i == j and guess.index(i) != key.index(j):
                print("Y", end='')
            elif i != j:
                print("R",end='')
    if guess == key:
        print("Game Over")
        continue

