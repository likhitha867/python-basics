i = 1
while i <= 5:
    if i % 2 == 0:          # when i is even…
        i += 1              # increment before continuing
        continue            # jump to the top of the loop
    print(i)
    i += 1