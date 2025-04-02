import graph
import kruskals_algorithm

vertices = 10
seed = 0.3
matrix = graph.generate_graph(vertices, seed)
adjacency_list = graph.convert_to_adjacency_list(matrix, vertices)
sorted_list = kruskals_algorithm.convert_adjecency_list_to_sorted_list(adjacency_list)
sorted_list_1 = kruskals_algorithm.convert_matrix_to_sorted_list(matrix, vertices)

if __name__ == "__main__":
    for e in matrix:
        print(e)

    for v in adjacency_list:
        print(f"{v} -> {adjacency_list[v]}")

    for pair in sorted_list:
        print(f"{pair[0]} -> {pair[1]}, weight - {pair[2]}")

    print("from matrix")
    for pair in sorted_list_1:
        print(f"{pair[0]} -> {pair[1]}, weight - {pair[2]}")