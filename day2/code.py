import numpy as np

def countSafe(inputFilename):
    safeNumber = 0
    row_lists = []

    with open(inputFilename, 'r') as file:
        for line in file:
            row = list(map(int, line.split()))
            row_lists.append(row)
        for i, row in enumerate(row_lists):
            #tmp = assessProblems(row) == set()
            tmp = assessProblemsWithTolerance(row) == set()
            safeNumber += tmp
      
    return safeNumber

# def assessProblems(list):
#     ''' returns the number of problems with a list ''' 
#     diff = np.diff(list)
#     # too much of a diff between two elements, regardless if positive or negative
#     if np.any(np.abs(diff) > 3):
#         return 0
#     # two adjacent elements are the same => bad
#     if np.any(diff==0):
#         return 0
#     # if all differences are positive or all negative, then it's good
#     if np.all(diff > 0):
#         return 1
#     if np.all(diff < 0):
#         return 1
#     return 0

def findDifferingSign(list):
    numPos = np.sum(list > 0)
    numNeg = np.sum(list < 0)
    if numPos > numNeg:
        return numPos
    else:
        return -numNeg

def assessProblems(list):
    # keep indices of problems, add to set, return indices
    diff = np.diff(list)
    problems = set()
    if np.all((diff > 0) & (diff < 3)): # within range
        return problems
    if np.all((diff < 0) & (diff > -3)): # within range
        return problems
    sign = findDifferingSign(diff)
    if sign > 0:
        problems.update(set(np.where(diff < 0)[0]))
    if sign < 0:
        problems.update(set(np.where(diff > 0)[0]))

    problems.update(set(np.where(diff > 3)[0]))
    problems.update(set(np.where(np.abs(diff) > 3)[0]))
    problems.update(set(np.where(diff == 0)[0]))
    
    return problems


def assessProblemsWithTolerance(list):

    problems = assessProblems(list)
    if problems != set() and len(problems) <= 1: ## only tolerate one issue, no more
        del list[problems.pop()] # check that this is correct
    else:
        return problems
    problems = assessProblems(list)
    return problems


# list = [7, 6, 4, 2, 1]# true
# list = [1, 2, 7, 8, 9]# false, 5
#list = [9, 7, 6, 2, 1]# false
# list = [1, 3, 2, 4, 5]# false
# list = [8, 6, 4, 4, 1]# false
#list = [1, 3, 6, 7, 9]# true

# list = [7, 6, 4, 2, 1] # true
#list = [1, 2, 7, 8, 9]# false
# list = [9, 7, 6, 2, 1]
# list = [1, 3, 2, 4, 5]
# list = [8, 6, 4, 4, 1]
# list = [1, 3, 6, 7, 9]
# list = [1,3,3,5,6]

# list= [48,46,47,49,51,54,56]
# list = [1, 1, 2, 3, 4, 5]
# list = [29, 28, 27, 25, 26, 25, 22, 20]
# list= [7, 10, 8, 10, 11]

# edge cases:
list = [9, 8, 7, 6, 7] # +1, 4
#                   *
#list = [29, 28, 27, 25, 26, 25, 22, 20] # +0, 3
#                     *

# tmp = assessProblems(list)
tmp = assessProblemsWithTolerance(list)
print('is safe:', tmp==set())

# inputFilename = "input.txt"
# print(countSafe(inputFilename))