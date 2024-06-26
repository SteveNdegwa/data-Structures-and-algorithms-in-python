class Vertex(object):
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.adj_list = []


class Graph(object):
    def __init__(self):
        self.vertex_list = []

    def search_vertex(self, name):
        if not self.vertex_list:
            return None
        for vertex in self.vertex_list:
            if vertex.name == name:
                return vertex
        return None

    def add_vertex(self, name):
        vertex_exists = self.search_vertex(name)
        if vertex_exists:
            return False
        new_vertex = Vertex(name)
        self.vertex_list.append(new_vertex)
        return True

    def remove_vertex(self, name):
        vertex = self.search_vertex(name)
        if not vertex:
            return False
        for v in vertex.adj_list:
            v.adj_list.remove(vertex)
        self.vertex_list.remove(vertex)
        return True

    def add_edge(self, name1, name2):
        vertex1 = self.search_vertex(name1)
        vertex2 = self.search_vertex(name2)
        if vertex1 and vertex2:
            vertex1.adj_list.append(vertex2) if vertex2 not in vertex1.adj_list else None
            vertex2.adj_list.append(vertex1) if vertex1 not in vertex2.adj_list else None
            return True
        return False

    def remove_edge(self, name1, name2):
        vertex1 = self.search_vertex(name1)
        vertex2 = self.search_vertex(name2)
        if vertex1 and vertex2:
            vertex1.adj_list.remove(vertex2) if vertex2 in vertex1.adj_list else None
            vertex2.adj_list.remove(vertex1) if vertex1 in vertex2.adj_list else None
            return True
        return False

    def bfs(self, root):
        root = self.search_vertex(root)
        queue = [root]
        if not root:
            return
        while queue:
            current = queue.pop(0)
            if current.visited:
                continue
            current.visited = True
            print(current.name)
            [queue.append(v) for v in current.adj_list]

    def dfs(self, root):
        root = self.search_vertex(root)
        if not root:
            return
        if root.visited:
            return
        root.visited = True
        [self.dfs(v.name) for v in root.adj_list]
        print(root.name)

    def print_graph(self):
        [print(vertex.name, [v.name for v in vertex.adj_list]) for vertex in self.vertex_list if self.vertex_list]


graph = Graph()
graph.add_vertex("thika")
graph.add_vertex("nairobi")
graph.add_vertex("nakuru")
graph.add_vertex("eldoret")
graph.add_vertex("mombasa")
graph.add_edge("thika", "nairobi")
graph.add_edge("nairobi", "nakuru")
graph.add_edge("eldoret", "nakuru")
graph.add_edge("nairobi", "mombasa")
graph.print_graph()
# graph.bfs("thika")
print()
graph.dfs("thika")

