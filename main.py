import time
import graph
import kruskals_algorithm

vertices = 6
seed = 0.3
matrix = graph.generate_graph(vertices, seed)
adjacency_list = graph.convert_to_adjacency_list(matrix, vertices)
sorted_list_from_adjecency_list = kruskals_algorithm.convert_adjecency_list_to_sorted_list(adjacency_list)
sorted_list__from_matrix = kruskals_algorithm.convert_matrix_to_sorted_list(matrix, vertices)

if __name__ == "__main__":

    for pair in sorted_list_from_adjecency_list:
        print(f"{pair[0]} <-> {pair[1]}, weight - {pair[2]}")

    start_time = time.time()
    minimum_spanning_tree = kruskals_algorithm.kruskals_algorithm(sorted_list_from_adjecency_list, vertices )
    end_time = time.time()
    execution_time = end_time - start_time

    print("\nMinimum spanning tree:")
    if len(minimum_spanning_tree) == 0:
        print("Sorry, graph is not connected. Minimum spanning tree doesn't exist")
    else:
        for edge in minimum_spanning_tree:
            print(f"{edge[0]} <-> {edge[1]}, weight - {edge[2]}")
        print(f"Execution time: {execution_time:.6f} seconds")