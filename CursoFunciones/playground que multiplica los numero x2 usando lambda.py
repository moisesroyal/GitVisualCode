def multiply_numbers(numbers):

    result = list(map(lambda number: number * 2, numbers))
    return result

numbers = [1, 2, 3, 4]
response = multiply_numbers(numbers)
print(response)