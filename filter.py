import re

with open('ancilla.txt','r') as IN:
    lines = IN.read().splitlines()

for line in lines:
    m = re.match(r'^(\w+[^,]+),\s+(\w+\D+)\s+(\d{4}).*?(\d+)(\s+)?$',line)
    print(f"{m.group(1)}\t{m.group(2)}\t\t\t\t\tBraun 2007: {m.group(4)}\t{m.group(3)}")
