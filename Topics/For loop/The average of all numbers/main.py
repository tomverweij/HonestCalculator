a = int(input())
b = int(input())

count_of_numbers = 0
sum_of_numbers = 0

for number in range(a, b + 1):
    if (number % 3) == 0:
        sum_of_numbers += number
        count_of_numbers += 1
print(sum_of_numbers / count_of_numbers)