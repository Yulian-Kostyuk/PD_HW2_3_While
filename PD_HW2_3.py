my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
a = 0
while a < len(my_list):
    element = my_list[a]
    if element > 0:
        print(element)
        a = a + 1
    elif element == 0:
        a = a + 1
    else:
        break

