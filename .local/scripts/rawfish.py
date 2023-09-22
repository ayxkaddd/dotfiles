#!/usr/bin/python3

import re 

input_file = '/home/ayx/.local/share/fish/fish_history'
output_file = '/home/ayx/.local/share/fish/fish_history.raw'

pattern = r'^- cmd:\s+(.*)$'

with open(input_file, 'r') as f:
    lines = f.readlines()


with open(output_file, 'w') as f:
    for line in lines:
        match = re.match(pattern, line)
        if match:
            cmd = match.group(1)
            f.write(cmd + '\n')

