import re

def main():
    hello_string="Hello, Python"
    print(hello_string)
    split_string = re.split(',|\s', hello_string)
    print('-'.join(split_string))



main()