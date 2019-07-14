import random
import sys

sys.setrecursionlimit(20000)
table = [[0 for _ in range(0, 9)]for _ in range(0, 9)]
numbers = [1,2,3,4,5,6,7,8,9]
loop = 0

def get_table():
    table = [[0 for _ in range(0, 9)]for _ in range(0, 9)]
    return table


def shuffle():
    shuffle_numbers = numbers[:]
    random.shuffle(shuffle_numbers)
    return shuffle_numbers


def elements_in_line(element):

    if element in range(0, 3):
        elements_to_compare = list(range(0, 3))
    elif element in range(3, 6):
        elements_to_compare = list(range(3, 6))
    else:
        elements_to_compare = list(range(6, 9))

    return elements_to_compare


def check_in_line(num_block, index_num, number):

    blocks_to_compare = elements_in_line(num_block)
    blocks_to_compare.remove(num_block)
    indx_num_to_compare = elements_in_line(index_num)

    for index in blocks_to_compare:
        for check_num in indx_num_to_compare:
            if number != table[index][check_num]:
                continue
            else:
                return False
    return True

def elements_in_column(element):

    if element in range(0, 7, 3):
        elements_to_compare = list(range(0, 7, 3))
    elif element in range(1, 8, 3):
        elements_to_compare = list(range(1, 8, 3))
    else:
        elements_to_compare = list(range(2, 9, 3))

    return elements_to_compare


def check_in_column(num_block, index_num, number):

    blocks_to_compare = elements_in_column(num_block)
    blocks_to_compare.remove(num_block)
    index_num_to_compare = elements_in_column(index_num)

    for index in blocks_to_compare:
        for check_num in index_num_to_compare:
            if number != table[index][check_num]:
                continue
            else:
                return False
    return True


def check_in_block(num_block, number):
    if not number in table[num_block]:
        return True
    else:
        return False


def make_table():
    global loop
    loop += 1
    if loop == 300:
        global table
        table = [[0 for _ in range(0, 9)]for _ in range(0, 9)]
        loop = 0
        return "reset"

    list_of_num = shuffle()
    list_blocks_for_make = [0,2,6,8,1,3,5,7,4]
    index = 0
    while list_blocks_for_make:
        while 0 in table[list_blocks_for_make[0]]:
            if index == 9:
                make_table()
            while index < 9:

                number = list_of_num[index]
                condition_1 = check_in_line(list_blocks_for_make[0], index, number)
                condition_2 = check_in_column(list_blocks_for_make[0], index, number)
                condition_3 = check_in_block(list_blocks_for_make[0], number)

                if condition_1 and condition_2 and condition_3:
                    table[list_blocks_for_make[0]][index] = number
                else:
                    index += 1
        list_blocks_for_make.pop(0)


def print_table():
    for i in range(0, 9, 3):
        print("")
        for j in range(0, 9, 3):
            print("{} {} {}  {} {} {}  {} {} {}".format(

                table[i + 0][j], table[i + 0][j + 1], table[i + 0][j + 2],
                table[i + 1][j], table[i + 1][j + 1], table[i + 1][j + 2],
                table[i + 2][j], table[i + 2][j + 1], table[i + 2][j + 2],
            ))
