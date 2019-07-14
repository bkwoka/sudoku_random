from uui import *


def start():
    res = make_table()
    if res == "reset":
        start()
    print_table()


if __name__ == "__main__":
    start()