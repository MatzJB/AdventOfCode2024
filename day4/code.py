import numpy as np
import re
inputFilename= 'input.txt'

def loadASCIIMatrix(inputFilename):
    ''' loads a matrix of characters into a matrix of ints '''
    with open(inputFilename, 'r') as file:
        lines = file.readlines()
    ascii_matrix = np.array([[ord(char) for char in line.strip()] for line in lines])
    return ascii_matrix

def search(matrix, pattern):
    ''' Looks for a string left to right, up to down, diagonally up and down and all reverse '''
    matrix = np.vstack([matrix, np.zeros(matrix.shape[1])])
    matrix = np.column_stack([matrix, np.zeros(matrix.shape[0])])
    flattened_rows = matrix.flatten(order='C') # row-major 
    flattened_rows = matrix.flatten(order='F') # column-major
    
    '''
    ABCD
    EFGH
    IJKL

    ABCD
     EFGH
      IJKL
    '''
    # create a new matrix to access diagonals

    
    # horisonal search:
    matrix[::-1]

    # vertical search:
    # reverse

    # diagonal up left to right:
    # reverse

    # diagonal down left to right
    #reverse

    
    matches = re.findall(pattern, text)
# up right to left
matrix = np.array([ [1,2,3,0],
                    [4,5,6,0],
                    [7,8,9,0],
                    [0,0,0,0]])

pattern = [ord(c) for c in "XMAS"]
# matrix = matrix+46
matrix = 13 + matrix.astype(np.uint8) 
#matrix = loadASCIIMatrix(inputFilename)



row_strings = ["".join(map(chr, row)) for row in matrix]
print(row_strings)
matches = re.findall(pattern, row_strings[0])




for i in range(1, matrix.shape[0]):
    matrix[i] = np.roll(matrix[i], i, axis=None)
matrix = matrix.transpose()
print(matrix)

