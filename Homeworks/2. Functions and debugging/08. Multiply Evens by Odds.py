def multiply_even_odds(number):
    evens = odds = 0
    for char in str(number):
        if int(char)%2:
            odds += int(char)
        else:
            evens += int(char)

    return evens*odds


num = abs(int(input()))
result = multiply_even_odds(num)
print(result)
