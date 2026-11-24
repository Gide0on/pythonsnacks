for hundreds_digit in range(1, 10):
    for tens_digit in range(0, 10):
        for ones_digit in range(0, 10):
            number = 100 * hundreds_digit + 10 * tens_digit + ones_digit
            sum_of_squares = hundreds_digit**2 + tens_digit**2 + ones_digit**2
            
            if sum_of_squares == number:
                print(number)
