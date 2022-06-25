##Find all occurrences of the given string in a character matrix
#Given an M × N matrix of characters, find all occurrences of a given string in the matrix. We are allowed to search the string in all eight possible directions, i.e., North, West, South, East, North-East, North-West, South-East, South-West. Note that there should not be any cycles in the output path.

directions = {
    "N": [0,-1],
    "NE": [1,-1],
    "E": [1,0],
    "SE": [1,1],
    "S": [0,1],
    "SW": [-1,1],
    "W": [-1,0],
    "NW": [-1,-1]
 }

def isValidCoordinate(mat, x, y, path):
    return (0 <= x < len(mat)) and (0 <= y < len(mat[0])) and (x, y) not in path           

def DFS(mat, word, i, j, path = [], index = 0):
    
    if mat[i][j] != word[index]:
        return

    path.append((i, j))
        
    if index == len(word) - 1:
        print(path) 
    else:
        for dir in directions.keys():
            if isValidCoordinate(mat, i + directions[dir][0], j + directions[dir][1], path):
                DFS(mat, word, i + directions[dir][0], j + directions[dir][1], path, index + 1)

    path.pop()


def findAllOccurences(mat, word):

    if not mat or not len(mat) or not len(word):
        return

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            DFS(mat, word, i, j)


     
