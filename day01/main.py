# file = open("./first.txt", "r")
# file = open("./second.txt", "r")
file = open("./puzzle_input.txt", "r")
array_lines = file.readlines()
acumulator = 0
first = None
last = None
flag = None
digits = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
        }

for line in array_lines:
    string = ""
    flag = None
    for c in line:
        if c.isnumeric():
            first = c
            break
        else:
            string = string + c
            for k, v in digits.items():
                if string.endswith(k):
                    first = v
                    flag = True
                    break
            if flag is not None:
                break
    string = ""
    flag = None
    for c in line[::-1]:
        if c.isnumeric():
            last = c
            break
        else:
            string = c + string
            for k, v in digits.items():
                if string.startswith(k):
                    last = v
                    flag = True
                    break
            if flag is not None:
                break

    calibration_value = str(first) + str(last)
    acumulator += int(calibration_value)

print(acumulator)
