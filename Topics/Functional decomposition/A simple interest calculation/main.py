def calculate(amount, interest_rate, time):
    interest = (amount * interest_rate * time) / 100
    total_amount = amount + interest
    return interest, total_amount

def print_result(interest, total_amount):
    print("The interest is: " + str(interest))
    print("The total amount is: " + str(total_amount))