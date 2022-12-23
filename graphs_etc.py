"""
Functions that provide various operations on graphs,
such as coloring, searching for Euler and Hamiltonian
cycles, checking for bipartiteness and graph coloring.
"""

import csv
import networkx as nx
import matplotlib.pyplot as plt

def read_csv(file_name: str) -> dict:
    """
    Reads csv file, returns graph as dictionary of lists
    """
    with open(file_name, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        lst = []
        graph = {}
        for row in csv_reader:
            vert = int(row[0]) - 1
            if vert not in lst:
                lst.append(vert)
                graph[vert] = []
            graph[vert].append(int(row[1]) - 1)
        for vert in lst:
            graph[vert] = sorted(graph[vert])

    return graph

def hamiltonian_cycle(graph):
    """
    dict -> str or list
    Checking if we can seach for Hamiltonian cycle
    >>> hamiltonian_cycle({0:[1,2,4], 1:[0,3], 2:[0,3,4], 3:[1,2,4], 4:[0,2,3]})
    [0, 1, 3, 2, 4, 0]
    >>> hamiltonian_cycle({0:[1,2,4], 1:[0,1,3], 2:[0,3,4], 3:[1,2,4], 4:[0,2,3]})
    'This graph has no Hamiltonian cycle'
    >>> hamiltonian_cycle({0:[1,2,4], 1:[0,3], 2:[0,3,4], 3:[1,2,4], 4:[0,1,2,3]})
    'This graph has no Hamiltonian cycle'
    >>> hamiltonian_cycle([[1,2,4], [0,3], [0,3,4], [1,2,4], [0,2,3]])
    'The graph is not set correctly'
    """
    if not isinstance(graph, dict):
        return ('The graph is not set correctly')
    path = []
    keys = list(graph.keys())
    for key in keys:
        if key in graph[key]:
            return "This graph has no Hamiltonian cycle"
    for key, value in graph.items():
        if len(value) == 0:
            return "This graph has no Hamiltonian cycle"
    all_vertex = [i for x in list(graph.values()) for i in x]
    for vert in list(graph.keys()):
        if all_vertex.count(vert) != len(graph[vert]):
            return "This graph has no Hamiltonian cycle"
    def cycle(graph,vertixes,root):
        """
        Creating path of Hamiltonian cycle
        """
        path.append(root)
        for el in graph[root]:
            if el not in path:
                if(cycle(graph,vertixes,el)):
                    return path

        if(len(path) == vertixes):
            if(path[0] in graph[path[-1]]):
                path.append(keys[0])
                return True 
            else:
                path.pop()
                return "This graph has no Hamiltonian cycle"
        path.pop()
    return cycle(graph,len(keys),keys[0])

def euler_cycle(graph):
    """
    Function for searching Euler cycle. The function returns cycle if\
 there is one, if not, it will return the appropriate message ('Graph \
has no Euler cycle'). If vertex in graph's value not in keys, function returns 'Vertex not in graph'
    >>> euler_cycle([1])
    >>> euler_cycle({1: [3], 2:[], 3:[5], 4:[1,2], 5:[2]})
    'Graph has no Euler cycle'
    >>> euler_cycle({1: [3,4], 2:[4,5], 3:[1,5], 4:[1,2], 5:[2,3]})
    [1, 3, 5, 2, 4, 1]
    >>> euler_cycle({1: [7,4], 2:[4,5], 3:[1,5], 4:[1,2], 5:[2,3]})
    'Vertex not in graph'
    >>> euler_cycle({'a': ['c','e'], 'b':['c','e'], 'c':['a','b','d','e'], 'd':['c','e'], \
'e':['a','b','c','d']})
    ['a', 'c', 'b', 'e', 'c', 'd', 'e', 'a']
    """
    if not isinstance(graph, dict):
        return None
    for key, value in graph.items():
        if len(value) == 0 or len (value) % 2 != 0 or key in graph[key]:
            return 'Graph has no Euler cycle'
    all_vertex = [i for x in list(graph.values()) for i in x]
    for vert in list(graph.keys()):
        if all_vertex.count(vert) != len(graph[vert]):
            return 'Vertex not in graph'
    #beginning of Euler cycle search
    euler_result=[]
    start = list(graph.keys())[0]
    euler_result.append(start)
    while True:
        vertex = euler_result[-1]
        for value in graph[vertex]:
            if len(graph[vertex]) != 1 and value == start:
                continue
            if value not in list(graph.keys()):
                return 'Vertex not in graph'
            euler_result.append(value)
            if vertex in graph[value]:
                graph[value].remove(vertex)
            graph[vertex].remove(value)
            break
        counter = 0
        for val in graph.values():
            if  val == []:
                counter += 1
        if len(list(graph.keys())) == counter:
            break
    if euler_result[0] != euler_result[-1]:
        return "Graph has no Euler cycle"
    return euler_result

def dvodolniy(graph):
    '''
    Take a graph and check whether it is дводольний

    >>> dvodolniy({1: [2, 3, 4], 2: [1, 5], 3: [1, 5], 4: [1], 5: [2, 3]})
    True
    >>> dvodolniy({1: [2, 3, 4, 5], 2: [1, 5], 3: [1, 5], 4: [1], 5: [2, 3]})
    False
    >>> dvodolniy({1: [1, 2, 3, 4, 5], 2: [1, 5], 3: [1, 5], 4: [1], 5: [2, 3]})
    False
    >>> dvodolniy({1: [2, 3], 2: [1, 3], 3: [1, 2]})
    False
    >>> dvodolniy({1: [2, 6], 2: [1, 3], 3: [2, 4], 4: [3, 1]})
    True
    >>> dvodolniy({1: [2, 6, 7], 2: [1, 3, 7], 3: [2, 4, 7], 4: [\
    3, 5, 7], 5: [6, 4, 7], 6: [1, 5, 7], 7: [1, 2, 3, 4, 5, 6]})
    False
    '''
    keys = list(graph.keys())
    lst1 = set()
    lst2 = set()

    # додаємо першу точку в лст1, щоб почати розподіл
    lst1.add(keys[0])

    # додаємо вельюс(суміжні точки до першої) в лст2
    for i in graph[keys[0]]:
        lst2.add(i)

    # проходимось по точках
    for i in keys[1:]:

        # якщо і в лст2, то перевіряємо чи не належать суміжні вершини цьому лісту
        # і додаємо їх в інший, якщо перша умова виконується
        if i in lst2:
            for elem in lst2:
                if graph[i] == elem:
                    return False
            for value in graph[i]:
                lst1.add(value)

        # аналогічно, якщо і в лст1
        elif i in lst1:
            for elem in lst1:
                if graph[i] == elem:
                    return False
            for value in graph[i]:
                lst2.add(value)

        # перевіряємо чи лст1 і лст2 не мають спільних елементів
        if lst1 & lst2:
            return False

    return True

def graph_coloring(graph):
    """
    Graph coloring function:
    The function accepts a connected graph and returns its coloring
    in three colors or a message about the impossibility of such
    coloring. Should return a list of vertex - color pairs.
    """
    vertices = [i[0] for i in graph.items()]
    # colors as numbers
    colors = [0]*len(vertices)
    # colors as str
    colors_str = ['red', 'blue', 'green']
    graph_matrix = [[0]*len(vertices) for _ in range(len(vertices))]
    final_coloring = []

    # make graph matrix
    for val in graph.items():
        for ver in vertices:
            if ver in val[1]:
                graph_matrix[val[0]][ver] = 1

    # check if matrix doesn't have zero row
    for row in graph_matrix:
        if 1 not in row:
            return "Unfortunately, coloring is impossible"

    def checkpoint(graph, color):
        """
        Check if color is safe to use
        """
        # check edges
        for index in range(len(vertices)):
            for jndex in range(index + 1, len(vertices)):
                if graph[index][jndex] and color[jndex] == color[index]:
                    return False
        return True

    def coloring_process(graph, col_num, index, color):
        """
        The coloring process itself
        """
        # final step
        if index == len(vertices):
            if checkpoint(graph, color) is True:
                final_coloring.append(color)
                return True
            return False

        # set color from 1 to col_num + 1
        for j in range(1, col_num + 1):
            color[index] = j
            if coloring_process(graph, col_num, index + 1, color) is True:
                return True
            color[index] = 0
        return False

    if coloring_process(graph_matrix, 3, 0, colors) is False:
        return "Unfortunately, coloring is impossible"

    final_coloring = list(final_coloring[0])
    output = [(key, colors_str[val-1]) for key, val in enumerate(final_coloring)]
    return output

def coloring_visualization(graph):
    """
    Function to visualize graph coloring
    :param graph dict: dictionary of vertices and edges
    :return None if everything works fine
    :return Unfortunately, coloring is impossible: in other case
    """
    # turn dict graph to list of edges
    list_of_edges = [(key, node) for key, val in graph.items() for node in val]
    network = nx.Graph()

    for egde in list_of_edges:
        network.add_edge(egde[0],egde[1])

    # color specific vertice
    pos = nx.spring_layout(network,seed=3113794652)
    colors = graph_coloring(graph)
    if not isinstance(colors, list):
        # check if coloring exists
        return colors

    red_colored = [i[0] for i in colors if i[1]=="red"]
    blue_colored = [i[0] for i in colors if i[1]=="blue"]
    green_colored = [i[0] for i in colors if i[1]=="green"]

    nx.draw_networkx_nodes(network, pos, nodelist=red_colored, node_color="tab:red")
    nx.draw_networkx_nodes(network, pos, nodelist=blue_colored, node_color="tab:blue")
    nx.draw_networkx_nodes(network, pos, nodelist=green_colored, node_color="tab:green")

    # color edges
    nx.draw_networkx_edges(
        network,
        pos,
        edgelist=list_of_edges,
        width=1,
        alpha=0.5,
        edge_color="tab:gray",
    )

    # add labels to the vertices
    labels = {i:str(i) for i in graph.keys()}
    nx.draw_networkx_labels(network, pos, labels, font_size=12, font_color="whitesmoke")
    plt.show()
