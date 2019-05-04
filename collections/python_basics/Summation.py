def summation(num):
    num = abs(num)
    num_list = []
    for n in range(1, num + 1):
        num_list.append(n)
    e = sum(num_list)

    print(e)


summation(8)

