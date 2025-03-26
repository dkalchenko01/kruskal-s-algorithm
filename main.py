import graph

vertices = 10
seed = 0.3
matrix = graph.generate_graph(vertices, seed)
adjacency_list = graph.convert_to_adjacency_list(matrix, vertices)

if __name__ == "__main__":
    for e in matrix:
        print(e)

    for v in adjacency_list:
        print(f"{v} -> {adjacency_list[v]}")