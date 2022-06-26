from trie import Trie

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


# Generate a list of possible words from a character matrix
# Given an M × N boggle board, find a list of all possible words that can be formed by a sequence of adjacent characters on the board. 
# 

def isValidCoordinate2(mat, x, y, path, key):
    return (0 <= x < len(mat)) and (0 <= y < len(mat[0])) and \
        (x, y) not in path and mat[x][y] == key

def searchBoggleDFS(mat, i, j, result, ch, root, path = []):
        

    if root.isLeaf:
        result.add(ch)

    path.append((i,j))

    for key, value in root.children.items():
        for dir in directions.keys():
            if isValidCoordinate2(mat, i + directions[dir][0], j + directions[dir][1], path, key):
                searchBoggleDFS(mat, i + directions[dir][0], j + directions[dir][1], result, ch + key, value)
                                
    
    path.pop()



def searchInBoggle(mat, words):

    if not mat or not len(mat) or not len(words):
        return

    result = set()

    root = Trie()
    for word in words:
        root.insert(word)  
 
    
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            ch = mat[i][j]

            if root.startWith(ch):              
                searchBoggleDFS(mat, i, j, result, ch, root.root.children[ch])

    print(result)


##Lexicographic sorting of a given set of keys
##Lexicographic sorting: Given a set of strings, return them in lexicographic order (dictionary/alphabetical order).





     
