import re

# with open('puzzle_input.txt', 'r') as f:
#     s = f.read()

with open('notsolvedyet.txt', 'r') as f:
    s = f.read()

red = 0
green = 0
blue = 0
id = 1
sum_ids = 0
for x in s.strip().split("\n"):
    red_per_game = re.findall(r"\d red", x)
    green_per_game = re.findall(r"\d green", x)
    blue_per_game = re.findall(r"\d blue", x)
    for r in red_per_game:
        r = int(r[0])
        red += r
    for g in green_per_game:
        g = int(g[0])
        green += g
    for b in blue_per_game:
        b = int(b[0])
        blue += b

    if red > 12 or green > 13 or blue > 14:
        break

    sum_ids += id

    red = 0
    green = 0
    blue = 0
    id += 1

print("Sum IDS:", sum_ids)
