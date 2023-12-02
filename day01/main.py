import re

# this pick text file line by line and put in array
# print(file.readlines())
def main():
    file = open("./puzzle_input.txt", "r")
    array_lines = file.readlines()
    acumulator = 0
    for line in array_lines:
        input = line
        reversed_input = input[::-1]
        first = find_first(input)
        last = find_last(reversed_input)
        if first and last:
            calibration_value = int(first + last)
            acumulator = acumulator + calibration_value
    return acumulator

def find_first(input):
    match = re.search(r'\d', input)
    if match:
        return match.group()
    else:
        return

def find_last(reversed_input):
    match = re.search(r'\d', reversed_input)
    if match:
        return match.group()[::-1]
    else:
        return

result = main()
print(result)


