import random

def generate_graph(n, p):

    vertices = list(range(n))
    edges = [[] * n for i in range(n)]

    for v in vertices:
        for j in range(v, n):
            if v == j:
                edges[v].append(None)
            elif random.random() < p:
                weight = random.randint(1, n)
                edges[v].append(weight)
                edges[j].append(weight)
            else:
                edges[v].append(None)
                edges[j].append(None)

    return edges

def convert_to_adjacency_list(edges, n):
    graph_dict = {}
    for i in range(n - 1):
        graph_dict[i] = []
        for j in range(0, n - 1):
            if edges[i][j] != None:
                graph_dict[i].append(j)

    return dict(sorted(graph_dict.items()))