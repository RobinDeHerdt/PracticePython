digits = int(input("How many digits should the sequence contain? \n"))

# Defaults
prev = 0
curr = 1

for digit in range(digits - 1):
    result = prev + curr
    print(result)

    # Prepare for the next loop
    prev = curr
    curr = result