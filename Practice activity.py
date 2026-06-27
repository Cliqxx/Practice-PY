# ==========================================
# PATTERN 1 - LEFT TRIANGLE
# ==========================================
# *
# **
# ***
# ****
# *****

n = int(input("Enter a number: "))

for i in range(1, n + 1):
    print("*" * i)


# ==========================================
# PATTERN 2 - INVERTED LEFT TRIANGLE
# ==========================================
# *****
# ****
# ***
# **
# *

for i in range(n, 0, -1):
    print("*" * i)


# ==========================================
# PATTERN 3 - TRIANGLE DIAMOND
# ==========================================
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

for i in range(1, n + 1):
    print("*" * i)

for i in range(n - 1, 0, -1):
    print("*" * i)


# ==========================================
# PATTERN 4 - CENTERED PYRAMID
# ==========================================
#     *
#    ***
#   *****
#  *******
# *********

for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))


# ==========================================
# PATTERN 5 - INVERTED PYRAMID
# ==========================================
# *********
#  *******
#   *****
#    ***
#     *

for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))


# ==========================================
# PATTERN 6 - HOLLOW RECTANGLE
# ==========================================
# *****
# *   *
# *   *
# *****

for i in range(5, 6):
    print("*" * i)

for i in range(3):
    print("*" + " " * 3 + "*")

for i in range(5, 6):
    print("*" * i)


# ==========================================
# PATTERN 7 - HOLLOW TRIANGLE
# ==========================================
# *
# **
# * *
# *  *
# *****

for i in range(1, n + 1):

    if i == 1 or i == 2 or i == n:
        print("*" * i)

    else:
        print("*" + " " * (i - 2) + "*")


# ==========================================
# PATTERN 8 - HOLLOW PYRAMID
# ==========================================
#     *
#    * *
#   *   *
#  *     *
# *********

for i in range(1, n + 1):

    if i == 1:
        print(" " * (n - 1) + "*")

    elif i == n:
        print("*" * (2 * n - 1))

    else:
        print(" " * (n - i) + "*" + " " * (2 * i - 3) + "*")


# ==========================================
# PATTERN 9 - NUMBER PYRAMID
# ==========================================
#     1
#    121
#   12321
#  1234321
# 123454321

for i in range(1, n + 1):

    print(" " * (n - i), end="")

    for j in range(1, i + 1):
        print(j, end="")

    for j in range(i - 1, 0, -1):
        print(j, end="")

    print()


# ==========================================
# PATTERN 10 - FLOYD'S TRIANGLE
# ==========================================
# 1
# 2 3
# 4 5 6
# 7 8 9 10

number = 1

for i in range(1, n + 1):

    for j in range(i):
        print(number, end=" ")
        number += 1

    print()


# ==========================================
# PATTERN 11 - REPEATED NUMBER TRIANGLE
# ==========================================
# 1
# 2 2
# 3 3 3
# 4 4 4 4

for i in range(1, n + 1):

    for j in range(i):
        print(i, end=" ")

    print()


# ==========================================
# PATTERN 12 - MULTIPLICATION TRIANGLE
# ==========================================
# 1
# 2 4
# 3 6 9
# 4 8 12 16

for i in range(1, n + 1):

    for j in range(1, i + 1):
        print(i * j, end=" ")

    print()


# ==========================================
# PATTERN 13 - NUMBER DIAMOND
# ==========================================
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1

for i in range(1, n + 1):

    for j in range(1, i + 1):
        print(j, end=" ")

    print()

for i in range(n - 1, 0, -1):

    for j in range(1, i + 1):
        print(j, end=" ")

    print()