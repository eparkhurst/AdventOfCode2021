with open('input.txt') as f:
    content = f.read().strip().split('\n')

input = [int(i) for i in content]

increases = 0
max = len(input) - 3
for i, value in enumerate(input):
    if(i < max):
        first_set = value + input[i+1] + input[i+2]
        second_set = input[i+1] + input[i+2] + input[i+3]
        if(first_set < second_set):
            increases += 1

print(increases)
