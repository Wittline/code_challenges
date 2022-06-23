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







    

    