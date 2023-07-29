#variables
number = 0
sum1 = 0
values = 0

print("To calculate the average of a series of numbers, please enter a sequence of numbers below. Enter '-1' to end sequence.")
while number != -1:
    number = int(input("Enter a number: "))
    sum1 += number
    values += 1

#calculating the average, excluding the -1
average = (sum1 + 1) / (values - 1)

print(f"The average of the numbers entered is {average}")