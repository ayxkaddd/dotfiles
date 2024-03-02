#!/usr/bin/python3
import sys

def encode_stuff(input_string):
    encoded_string = ""
    for char in input_string:
        encoded_string += f"\\{ord(char):03o}"
    return encoded_string

str_ = ' '.join(sys.argv[1::])
res = encode_stuff(str_)
print(res.replace("\\040", " "))
