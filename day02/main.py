with open('puzzle_input.txt', 'r') as f:
    s = f.read()

game_number = 1
possible = True
sum_ids = 0
sum_sets = 0
for line in s.strip().split("\n"):
    possible = True
    line = line.split(":")
    game = line[0]
    power = 1
    maxColors = {
            "red": 0,
            "green": 0,
            "blue": 0
            }
    for random in line[1].split(";"):
        for cubes in random.split(","):
            cubes = cubes.strip().split(" ")
            amount = int(cubes[0])
            color = cubes[1]
            if maxColors[color] < amount:
                maxColors[color] = amount
            if amount > 12 and color == 'red':
                possible = False
            if amount > 13 and color == 'green':
                possible = False
            if amount > 14 and color == 'blue':
                possible = False

    if maxColors:
        power *= maxColors["red"] * maxColors["blue"] * maxColors["green"]
        sum_sets += power

    if possible == True:
        sum_ids += game_number

    
    game_number += 1


print("Sum ids:", sum_ids)
print("Sum sets:", sum_sets)
