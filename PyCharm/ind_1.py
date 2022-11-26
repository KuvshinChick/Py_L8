#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    # Ввод значений
    c_1 = tuple(map(int, input("Goals in first championship : ").split()))
    c_2 = tuple(map(int, input("Goals in first championship : ").split()))

    # Проверка кол-ва игр
    if len(c_1) != 26 or len(c_2) != 26:
        print("Invalid tuple size ", file=sys.stderr)
        exit(1)

    # Проверка отрицательных значений
    for i in c_1:
        if i < 0:
            print("Negative value ", file=sys.stderr)
            exit(1)

    for i in c_2:
        if i < 0:
            print("Negative value ", file=sys.stderr)
            exit(1)

    # Поиск общего кол-ва мячей
    s = 0
    for i in c_1:
        s += i
    for i in c_2:
        s += i

    print(f"Total number of goals = {s}")
