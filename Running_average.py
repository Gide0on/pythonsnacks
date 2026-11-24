total = 0
count = 0

while True:
    number = float(input("Enter a number (-1 to stop): "))

    if number == -1:
        break

    total += number
    count += 1
    running_average = total / count
    print(f"Running average: {running_average:.2f}")
