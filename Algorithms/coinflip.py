import random

number_of_flips = int(input("How many coin flips would you like to execute? \n"))

heads_result = 0
tails_result = 0

for flip in range(number_of_flips):
    if random.randrange(0,2) < 1:
        print('Heads')
        heads_result += 1
    else:
        print('Tails')
        tails_result += 1

print("*** Results ***")
print("Heads: ", heads_result)
print("Tails: ", tails_result)