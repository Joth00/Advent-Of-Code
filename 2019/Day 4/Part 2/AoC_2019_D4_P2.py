# Advent of Code 2019, Day 4, Part 2
# Author: Joth (https://github.com/joth00)


def main():
    value_range = (245182, 790572)

    number_of_passwords = 0

    for value in range(value_range[0], value_range[1] + 1):
        text_value = str(value)
        if contains_exact_double_digit(text_value) and digits_never_decrease(text_value):
            number_of_passwords += 1
    
    print(number_of_passwords)


def contains_exact_double_digit(text_number):
    for i in range(len(text_number) - 1):
        if (text_number[i] == text_number[i + 1]
                and text_number.count(text_number[i]) == 2):
            return True
    return False


def digits_never_decrease(text_number):
    for i in range(len(text_number) - 1):
        if text_number[i] > text_number[i + 1]:
            return False
    return True


main()
