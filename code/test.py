from mygraph import myGraph

g = { "a" : {"d"},
      "b" : {"c"},
      "c" : {"b", "c", "d", "e"},
      "d" : {"a", "c"},
      "e" : {"c"},
      "f" : {}
    }

graph = myGraph(g)

print(graph.all_vertices())
print(graph.all_edges())
