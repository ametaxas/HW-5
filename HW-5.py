import re

file_name = input('Enter the file name:')
nums_str = re.findall(r'[0-9]+', open(file_name, 'r').read())
nums_int = [int(num) for num in nums_str]
print (sum(nums_int))