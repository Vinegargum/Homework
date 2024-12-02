my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
length = len(my_list)
number = -1
while number < length:
    if my_list[number + 1] > 0:
        print(my_list[number + 1])
        number = number + 1
    elif my_list[number + 1] == 0:
        number = number + 1
        continue
    else:
        break
