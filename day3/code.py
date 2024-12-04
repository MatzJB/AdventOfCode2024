
import re

inputFilename = 'input2.txt'

def sumofMults(inputFilename):

    row_list = []
    pattern = r"\((-?\d+),(-?\d+)\).*?"
    sum = 0

    with open(inputFilename, 'r') as file:
        content = file.read()
        content = content.replace("m\nul", "").replace("mu\nl", "")

 for line in content.splitlines():
        line = line.strip()  # Remove leading/trailing whitespace
        subline = line.split('mul')  # Split by "mul"
        
        for i, sub in enumerate(subline):
            if i == 0:
                row_list.append(sub.strip())  # First part, no "mul" prepended
            else:
                row_list.append('mul' + sub.strip())  # Prepend "mul" to others


        for line in file:
            subline = line.split('mul')
            for sub in subline:
                row_list.append('mul' + sub) # trim right
        
        print(len(row_list))
        
        for row in row_list:
            match = re.search(pattern, row)
            if match:
                print(f' MATCH: {row}')
                x, y = match.groups()
                print(x, y)
                sum += int(x)*int(y)
            else:
                print(f'did not match: {row}')

    return sum


s = sumofMults(inputFilename)
print(s)