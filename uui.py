import random

table = [[0] * 9] * 9
numbers = [num for num in range(1, 10)]


def shuffle():

    shuffle_numbers = numbers[:]
    random.shuffle(shuffle_numbers)

    return shuffle_numbers


def check_in_line(num_block, number):
    if num_block in range(0, 3):
        block_to_compare = list(range(0, 3))
        block_to_compare.remove(num_block)






def check_in_column():
    pass

def check_in_block():
    pass


def make_table():
    list_of_num = shuffle()
    list_blocks_for_make = [2]
    while list_of_num:
        for index, number in enumerate(list_of_num):
            check_in_line(list_blocks_for_make[0], list_of_num[index])


def print_table():
    for i in range(0, 9, 3):
        print("")
        for j in range(0, 9, 3):
            print("{} {} {}  {} {} {}  {} {} {}".format(

                table[i + 0][j], table[i + 0][j + 1], table[i + 0][j + 2],
                table[i + 1][j], table[i + 1][j + 1], table[i + 1][j + 2],
                table[i + 2][j], table[i + 2][j + 1], table[i + 2][j + 2],
            ))
