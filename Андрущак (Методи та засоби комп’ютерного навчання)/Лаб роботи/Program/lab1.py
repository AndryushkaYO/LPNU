import random

# TASK 1
print("<---   TASK 1 --->")


def convert_c_to_f(degree):
    return (degree * 1.8) + 32


for i in range(20, 36, 2):
    print(i, "℃  ---> ", "%.f" % convert_c_to_f(i), "℉")

print("\nOdd numbers:")
product = 1
for i in range(1, 21+1):
    if i % 2 != 0:
        print(i, end=" ")
        product *= i

print("\nProduct:", product)

# TASK 2
print("\n\n<---   TASK 2 --->")


def print_calendar(days_amount, start_day):
    for j in range(start_day):
        print("  ", end=" ")
    for i in range(1, days_amount+1):
        if i < 10:
            print("", i, end=" ")
        else:
            print(i, end=" ")
        if(i+start_day) % 7 == 0:
            print("")
    print("")


for i in range(5):
    n = int(input("Input the number of days in the month (28-31): "))
    d = int(input("Input the starting day (0=Sun, 1=Mon,...):"))
    print_calendar(n, d)

print("\nEven numbers [-3;-25]:")
i = -3
while i >= -25:
    if i % 2 == 0:
        print(i, end=" ")
    i -= 1

# TASK 3
print("\n\n<---   TASK 3 --->")


def create_random_list(size):
    arr = list(range(size))
    random.shuffle(arr)
    return arr


def get_max_value_index(values_list):
    max = values_list[0]
    max_index = 0
    for i in range(len(values_list)):
        if max < values_list[i]:
            max = values_list[i]
            max_index = i
    return max_index


def shell_sort(values_list):
    n = len(values_list)
    step = round(n / 2)
    while step > 0:
        for i in range(step, n):
            temp = values_list[i]
            j = i
            while j >= step and values_list[j - step] > temp:
                values_list[j] = values_list[j - step]
                j -= step
            values_list[j] = temp
        step = round(step / 2)
    return values_list


numbers_1 = create_random_list(12)
print("List of numbers: ", end="")
print(numbers_1)
print("Index of max number: ", get_max_value_index(numbers_1))

numbers_2 = create_random_list(50)
print("\nList of numbers: ", numbers_2)
print("Sorted list of numbers: ", end="")
print(shell_sort(numbers_2))
