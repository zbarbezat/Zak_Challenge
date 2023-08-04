import re
import sys

def validate_number(num):
    """ validate credit card number based on criteria provided """
    # check if meets groups of four digits followed by hyphen format or just 16 digits
    if not re.match(r'((\d{4}-){3}\d{4}$|(\d{16}$))', num):
        return False
    # check if starts with 4, 5, or 6
    if not re.match(r'^[4-6]', num):
        return False
    # check for 4 or more repeating digits, removing hyphens to cover case where repeating digit inbetween hyphens
    if re.search(r'(\d)\1{3,}', num.replace('-','')):
        return False
    
    return True

# read from stdin, skipping first input integer
infile = sys.stdin
next(infile)

for num in infile:
    if validate_number(num):
        print('Valid')
    else:
        print('Invalid')
