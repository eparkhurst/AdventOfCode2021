with open("input.txt") as f:
    content = f.read().strip().split("\n")

counts = [0] * len(content[0])

for line in content:
    for i, char in enumerate(line):
        counts[i] += int(char)

half = len(content) / 2
gama = ""
epsilon = ""
for count in counts:
    if count > half:
        gama += "1"
        epsilon += "0"
    else:
        gama += "0"
        epsilon += "1"

print(int(gama, 2) * int(epsilon, 2))
