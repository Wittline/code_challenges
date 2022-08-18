# Tree edge (u, v): departure[u] > departure[v]
# Back edge (u, v): departure[u] < departure[v]
# Forward edge (u, v): departure[u] > departure[v]
# Cross edge (u, v): departure[u] > departure[v]

def __dfs_run_2(self, vertex, visited_departure, time):

    visited_departure[vertex][0] = True

    for v in self._graph_dict[vertex]:
        if visited_departure[v][0] == False:
            time = self.__dfs_run_2(v, visited_departure, time)
    
    visited_departure[vertex][1] = time
    time = time + 1

    return  time


def isDag(self):

    visited_departure = {k:[False,None] for k in self._graph_dict}

    time = 0

    for vertex in self._graph_dict:
        if not visited_departure[vertex][0]:
            time = self.__dfs_run_2(vertex, visited_departure, time)

    for vertex in self._graph_dict:
        for vertex_connected in self._graph_dict[vertex]:

            if visited_departure[vertex][1] <= visited_departure[vertex_connected][1]:
                return False

    return True