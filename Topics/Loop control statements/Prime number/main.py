number = int(input())
number_of_divisions = 0


for i in range(1, number + 1):
    # print(str(number) + " % " + str(i) + " = " + str(number % i))
    if number % i == 0:
        number_of_divisions += 1

print("This number is not prime" if number_of_divisions != 2 else "This number is prime")
