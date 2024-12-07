import copy
import math
import matplotlib
import matplotlib.pyplot as plt

inputFilename = 'input.txt'

def load_file_to_list_of_lists(file_path):
    with open(file_path, 'r') as file:
        return [list(line.strip()) for line in file]

def findChar(llist, char):
    rows = len(llist)
    columns = len(llist[0])
    for i in range(rows):
        for j in range(columns):
            if llist[i][j] == char:
                return [i,j]
    return [-1,-1]

def updateDirection(currentAngle):
    theta = currentAngle + 90 # convert from unit circle to matrix directions
    theta = theta*math.pi/180.0
    dx = round(math.cos(theta))
    dy = round(math.sin(theta))
    return [dx, dy]

def countCharacter(llist, char):
    return sum(row.count(char) for row in llist)

def remove_special_chars(list_of_lists):
    ''' for visualizing with matplotlib '''
    return [[char for char in row if char.isalnum()] for row in list_of_lists]

def convert_to_floats(llist):
    ''' Just to visualize with matplotlib '''
    A = copy.deepcopy(llist)
    rows = len(A)
    columns = len(A[0])
    for i in range(rows):
        for j in range(columns):
            if A[i][j] == '.':
                A[i][j] = 0
            elif A[i][j] == '#':
                A[i][j] = 10
            elif A[i][j] == '^':
                A[i][j] = 2
            elif A[i][j] == 'X':
                A[i][j] = 5
            else:
                A[i][j]=17
    return [[float(char) for char in row] for row in A]

rotationAngle = 90
llist = load_file_to_list_of_lists(inputFilename)
pos = findChar(llist, '^')
step = updateDirection(rotationAngle)
rows, columns = len(llist), len(llist[0])
nextPos = copy.deepcopy(pos)

while nextPos[0]>=0 and nextPos[0] < rows and nextPos[1]>=0 and nextPos[1]<columns:
    if llist[nextPos[0]][nextPos[1]] == '#':
        rotationAngle -=90
        step = updateDirection(rotationAngle)
        rotationAngle = rotationAngle%360 # we need to map the angle to [0, 360]
       
    pos[0] = pos[0] + step[0]
    pos[1] = pos[1] + step[1]
    llist[pos[0]][pos[1]] = 'X'
    llist[pos[0]][pos[1]] = 'X'    
    nextPos[0] = pos[0] + step[0]
    nextPos[1] = pos[1] + step[1]
positions = countCharacter(llist, 'X')
print(f'positions {positions}')

figMatrix = plt.matshow(convert_to_floats(llist))
plt.show()
print('test')





