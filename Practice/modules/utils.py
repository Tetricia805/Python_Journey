# loop through the list to find the highest nyumber

def find_maximum(numbers):
    max_num = numbers[0]

    for number in numbers:
        if number > max_num:
            max_num = number

    return max_num


