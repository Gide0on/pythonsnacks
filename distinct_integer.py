Value = int(input("Enter target value: "))

for firstNumber in range(1, 10):

    for secondNumber in range(firstNumber + 1, 10):

        for thirdNumber in range(secondNumber + 1, 10):

            if firstNumber + secondNumber + thirdNumber == Value:

                print(firstNumber, "+", secondNumber, "+", thirdNumber, "=", Value)
