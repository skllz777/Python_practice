digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for digit in digits:
    if digit == 1:
        print(f"{digit}st")
    elif digit == 2:
        print(f"{digit}nd")
    elif digit == 3:
        print(f"{digit}rd")
    else:
        print(f"{digit}th")