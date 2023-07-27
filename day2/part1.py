with open("input.txt") as f:
    content = f.read().strip().split("\n")

vertical, horizontal = 0, 0
for input in content:
    direction, value = input.split(" ")
    if direction == "forward":
        horizontal += int(value)
    elif direction == "up":
        vertical -= int(value)
    elif direction == "down":
        vertical += int(value)

print(vertical * horizontal)
