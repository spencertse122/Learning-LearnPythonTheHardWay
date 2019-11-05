def lub_the_loop(n):

    i = 0
    numbers = []

    while i < n:
        # print(f"At the top i is {i}")
        numbers.append(i)

        i = i + 1
        # print("Numbers now: ", numbers)
        # print(f"At the bottom i is {i}")
        # print('-' * 20)

    # print("The numbers: ")
    # for num in numbers:
    #     print(num)

    return numbers

test_num = lub_the_loop(6)

print('-' * 20)
for i in test_num:
    print(i)
