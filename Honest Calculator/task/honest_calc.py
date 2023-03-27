msg_ = []
msg_.append("Enter an equation")
msg_.append("Do you even know what numbers are? Stay focused!")
msg_.append("Yes ... an interesting math operation. You've slept through all classes, haven't you?")
msg_.append("Yeah... division by zero. Smart move...")
msg_.append("Do you want to store the result? (y / n):")
msg_.append("Do you want to continue calculations? (y / n):")
msg_.append(" ... lazy")
msg_.append(" ... very lazy")
msg_.append(" ... very, very lazy")
msg_.append("You are")
msg_.append("Are you sure? It is only one digit! (y / n)")
msg_.append("Don't be silly! It's just one number! Add to the memory? (y / n)")
msg_.append("Last chance! Do you really want to embarrass yourself? (y / n)")

memory = float(0)

def read_calc():
    print(msg_[0])
    return input()

def is_one_digit(number):
    if number.is_integer() and number > -10 and number < 10:
        return True
    else:
        return False

def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_[6]
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg = msg + msg_[7]
    if (v1 == 0 or v2 == 0) and v3 in "*+-":
        msg = msg + msg_[8]
    if msg != "":
        msg = msg_[9] + msg
        print(msg)

while True:
    try:
        # get input
        x, oper, y = read_calc().split()

        # check usage of memory 'M'
        if x == 'M':
            x = memory
        else:
            x = float(x)
        if y == 'M':
            y = memory
        else:
            y = float(y)

        # check operand
        if oper not in '+-*/':
            print(msg_[2])
            continue
        else:
            check(x, y, oper)

        # perform operation
        if oper == "+":
            result = x + y
        elif oper == '-':
            result = x - y
        elif oper == '*':
            result = x * y
        elif oper == '/':
            result = x / y

        print(result)

        # ask to store in memory
        print(msg_[4])
        if input() == 'y':
            store_memory = True
            # yes we want to store in memory... but
            # doublecheck if this is not silly (3 passes)
            if is_one_digit(result):
                msg_index = 10
                while msg_index <= 12:
                    print(msg_[msg_index])
                    if input() == 'n':
                        store_memory = False
                        break
                    msg_index += 1
            if store_memory:
                memory = result

        # and ask if continue
        print(msg_[5])
        if input() == 'n':
            break

    except ValueError:
        print(msg_[1])
    except ZeroDivisionError:
        print(msg_[3])


