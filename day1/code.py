inputFilename = "input.txt"

def readFile(inputFilename):
    
    list1 = []
    list2 = []

    with open(inputFilename, "r") as f:
        for line in f:
            tup = list(map(int, line.split('   ')))
            list1.append(tup[0])
            list2.append(tup[1])
    
    return list1, list2

# subproblem 1
def sumDiff(inputFilename):
    list1, list2=readFile(inputFilename)
    list1.sort()
    list2.sort()

    diff = [abs(a - b) for a, b in zip(list1, list2)]
    return sum(diff)

# subproblem 2
def similarityScore(inputFilename):
    score = 0
    list1, list2 = readFile(inputFilename)
    for val in list1:
        score += val*list2.count(val)
    return score

s = sumDiff(inputFilename)
print(f'sum of differences: {s}')
sc=similarityScore(inputFilename)
print(f'similarity score {sc}')
