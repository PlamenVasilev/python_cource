def sign_of_number(num):
    if num > 0:
        print(f'The number {num} is positive.')
    elif num < 0:
        print(f'The number {num} is negative.')
    else:
        print(f'The number {num} is zero.')



num = int(input())
sign_of_number(num)