def find_max(numbers):
    many = numbers[0]
    for number in numbers:
        if number > many:
            many = number
    return many
