class myGraph:

    def __init__(self, graph_dict = None):
        
        if graph_dict == None:
            graph_dict = {}
        self._graph_dict = graph_dict

    def all_vertices(self):
        return set(self._graph_dict.keys())

    def all_edges(self):
        edges = []
        for vertex in self._graph_dict:
            for vertex_connected in self._graph_dict[vertex]:
                if {vertex, vertex_connected} not in edges:
                    edges.append({vertex, vertex_connected})
        return edges

    def edges(self, vertice):
        return self._graph_dict[vertice]    

    def add_vertex(self, vertex):
        if vertex not in self._graph_dict:
            self._graph_dict[vertex] = []

    def add_edge(self, vertices):

        if len(vertices) == 2:
            for vertex in vertices:
                if vertex not in self._graph_dict:
                    return
            self._graph_dict[vertices[0]].add(vertices[1])
        else:
            print("only two vertices are allowed")

    def find_path(self, vertex_start, vertex_end, path = None):

        if path == None:
            path = []

        path = path + [vertex_start]

        if vertex_start == vertex_end:
            return path
        
        if vertex_start not in self._graph_dict:
            return None
        
        for vertex in self._graph_dict[vertex_start]:
            if vertex not in path:
                _path = self.find_path(vertex, vertex_end, path)

                if _path:
                    return _path
        
        return None

    def find_all_paths(self, vertex_start, vertex_end, path = None):

        if path == None:
            path = []
        
        path = path + [vertex_start]

        if vertex_start == vertex_end:
            return [path]
        
        if vertex_start not in self._graph_dict:
            return []

        paths = []
        
        for vertex in self._graph_dict[vertex_start]:
            if vertex not in path:
                _path = self.find_all_paths(vertex, vertex_end, path)

                for p in _path:
                    paths.append(p)

        return paths


    def vertex_degree(self, vertex):

        degree = len(self._graph_dict[vertex])

        for vertex in self._graph_dict[vertex]:
            degree += 1
        
        return degree

    
    def get_isolated_vertices(self):

        isolated = []

        for vertex in self._graph_dict:
            if not self._graph_dict[vertex]:
                isolated += [vertex]

        return isolated
    
    
    def BFS(self, vertex):

        visited = {k:False for k in self._graph_dict}
        queue = []

        queue.append(vertex)
        visited[vertex] = True

        while queue:
            vertex = queue.pop(0)
            print(vertex, end = "")

            for vertex_connected in self._graph_dict[vertex]:
                if visited[vertex_connected] == False:
                    visited[vertex_connected] = True
                    queue.append(vertex_connected)


    def __dfs_run(self, vertex, visited):
        visited[vertex] = True
        print(vertex, end=' ')

        for vertex_connected in self._graph_dict[vertex]:
            if visited[vertex_connected] == False:
                self.__dfs_run(vertex_connected, visited)
                
    
    def DFS(self, vertex):
        visited = {k:False for k in self._graph_dict}

        self.__dfs_run(vertex, visited)

    
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



















    

    