from mygraph import myGraph
import dfs_examples


# g = { "a" : {"d"},
#       "d" : {"c"},
#       "c" : {"f"},
#       "d" : {"f"},
#       "f" : {}
#     }

# gph = myGraph(g)
# print(gph.isDag())
# print(gph.topological_sort())

# mat = [
#     ['D', 'E', 'M', 'X', 'B'],
#     ['A', 'O', 'X', 'P', 'E'],
#     ['X', 'X', 'C', 'X', 'D'],
#     ['X', 'D', 'X', 'D', 'S'],
#     ['C', 'O', 'Y', 'E', 'N']
# ]

# word = 'CODE'

# dfs_examples.findAllOccurences(mat, word)


board = [
    ['M', 'S', 'E', 'F'],
    ['R', 'A', 'T', 'D'],
    ['L', 'O', 'N', 'E'],
    ['K', 'A', 'F', 'B']
]

words = ['START', 'NOTE', 'SAND', 'STONED']

dfs_examples.searchInBoggle(board, words)



