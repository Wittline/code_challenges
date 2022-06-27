def __dfs_cycle(self, source, visited, parent = None):

    visited[source] = True

    for vertex in self._graph_dict[source]:

        if not visited[vertex]:
            if self.__dfs_cycle(vertex, visited, source):
                return True
        elif vertex != parent:
            return True
                                        
    return False


def has_cycle(self):

    visited = {k:False for k in self._graph_dict}
    return self.__dfs_cycle("a", visited)