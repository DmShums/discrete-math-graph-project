"""
Functions that provide various operations on graphs,
such as coloring, searching for Euler and Hamiltonian
cycles, checking for bipartiteness and graph coloring.
"""

import csv
import networkx as nx
import matplotlib.pyplot as plt


def read_csv(file_name):
    """
    Reads csv file, returns graph as dictionary of lists
    """
    with open(file_name, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        i = 0
        graph = {}
        for row in csv_reader:
            graph[i] = row
            i = i + 1

    return graph

def hamiltonian_cycle(graph):
    """
    dict -> str, list
    Checking if we can seach for Hamiltonian cycle
    >>> hamiltonian_cycle({0:[1,2,4], 1:[0,3], 2:[0,3,4], 3:[1,2,4], 4:[0,2,3]})
    Hamiltonian cycle:
    [0, 1, 3, 2, 4, 0]
    >>> hamiltonian_cycle({0:[1,2,4], 1:[0,1,3], 2:[0,3,4], 3:[1,2,4], 4:[0,2,3]})

    >>> hamiltonian_cycle({0:[1,2,4], 1:[0,3], 2:[0,3,4], 3:[1,2,4], 4:[0,1,2,3]})
    """
    pass

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
    pass

def graph_coloring(graph):
    """
    Graph coloring function:
    The function accepts a connected graph and returns its coloring
    in three colors or a message about the impossibility of such
    coloring. Should return a list of vertex - color pairs.
    """
    pass

def coloring_visualization(graph):
    """
    Function to visualize graph coloring
    :param graph dict: dictionary of vertices and edges
    :return None if everything works fine
    :return Unfortunately, coloring is impossible: in other case
    """
    pass
