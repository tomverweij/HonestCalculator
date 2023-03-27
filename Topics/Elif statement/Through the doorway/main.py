length = int(input())
width = int(input())
height = int(input())
door_width = int(input())
door_height = int(input())

fit_count = 0

if length <= door_height and length <= door_width:
    fit_count += 1
if width <= door_height and width <= door_width:
    fit_count += 1
if height <= door_height and height <= door_width:
    fit_count += 1

if fit_count >= 2:
    print("The box can be carried")
else:
    print("The box cannot be carried")
