
import re

file = open("regex_sum_1806427.txt", 'r')

all_data = file.read()

# This output all values as list separated commas
line_values = re.findall('[0-9]+', all_data)

sum = 0
for value in line_values:
    sum = sum + int(value)

print(f"In file total of the number list is {sum}")
