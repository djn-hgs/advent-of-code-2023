with open('demo.txt', 'r') as file:
    lines = file.readlines()

print(lines)
print([''.join(list(x)) for x in zip(*lines)])



