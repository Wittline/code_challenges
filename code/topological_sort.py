def __topo_sort(self, vertex, visited, stack):

    visited[vertex] = True

    for v in self._graph_dict[vertex]:
        if visited[v] == False:
            self.__topo_sort(v, visited, stack)

    stack.insert(0, vertex)


def topological_sort(self):

    visited = {k:False for k in self._graph_dict}

    stack = []

    for vertex in self._graph_dict:     
        if visited[vertex] == False:
            self.__topo_sort(vertex, visited, stack)
    
    return stack