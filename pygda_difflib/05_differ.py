import difflib

with open('first') as file:
    first = file.readlines()

with open('second') as file:
    second = file.readlines()


differ = difflib.Differ()

result = list(differ.compare(first, second))
for line in result:
    print(line, end='')
