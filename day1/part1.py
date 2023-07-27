with open("input.txt") as f:
    content = f.read().strip().split("\n")

input = [int(i) for i in content]

increases = 0
length = len(input)
for i, value in enumerate(input):
    if i < length - 1:
        if value < input[i + 1]:
            increases += 1

print(increases)
