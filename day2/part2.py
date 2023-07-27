with open("input.txt") as f:
    content = f.read().strip().split("\n")

vertical = 0
horizontal = 0
aim = 0
for input in content:
    direction, value = input.split(" ")
    if direction == "forward":
        horizontal += int(value)
        vertical += aim * int(value)
    elif direction == "up":
        aim -= int(value)
    elif direction == "down":
        aim += int(value)

print(vertical * horizontal)
