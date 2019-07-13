import random

table = [[0] * 9] * 9

numbers = [i for i in range(1, 10)]

def shuffle():

    shuff_numbers = numbers[:]
    random.shuffle(shuff_numbers)

    return shuff_numbers


table[0] = shuffle()
table[8] = shuffle()

for i in range(0, 9, 3):
    print("")
    for j in range(0, 9, 3):
        print("{} {} {}  {} {} {}  {} {} {}". format(

            table[i + 0][j], table[i + 0][j + 1], table[i + 0][j + 2],
            table[i + 1][j], table[i + 1][j + 1], table[i + 1][j + 2],
            table[i + 2][j], table[i + 2][j + 1], table[i + 2][j + 2],
        ))

