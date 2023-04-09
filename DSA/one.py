#!/usr/bin/python3
rows = int(input("please enter row value"))
for i in range(rows):
    # nested loop
    for j in range(i):
        # display number
        print(i, end=' ')
    # new line after each row
    print('')
