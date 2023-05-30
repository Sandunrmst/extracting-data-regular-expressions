import re
import urllib.request

url = 'https://py4e-data.dr-chuck.net/regex_sum_1806427.txt'
response = urllib.request.urlopen(url)
data = response.read().decode('utf-8')

sum = 0
string_list_of_numbers = re.findall('[0-9]+', data)

for value in string_list_of_numbers:
    sum += int(value)

print(f"In file total of the number list is {sum}")
