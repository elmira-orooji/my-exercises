# get inputs ( work , university , both)
w , s , i = map(int, input().split())


# Calculate break time
total = ( w + s ) - i
nima_break_time = 24 - total 

print(nima_break_time)