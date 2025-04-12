import time
import csv
import graph
import kruskals_algorithm

vertices = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200]
seed = [0.4, 0.5, 0.6, 0.7, 0.8]

if __name__ == "__main__":

    with open('kruskals_results.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Size', 'Seed', 'MatrixOrList', 'Time'])


        for v in vertices:
            for s in seed:
                for i in range(20):
                    matrix = graph.generate_graph(v, s)
                    adjacency_list = graph.convert_to_adjacency_list(matrix, v)
                    sorted_list_from_adjecency_list = kruskals_algorithm.convert_adjecency_list_to_sorted_list(
                        adjacency_list)
                    sorted_list_from_matrix = kruskals_algorithm.convert_matrix_to_sorted_list(matrix, v)

                    start_time_list = time.time()
                    minimum_spanning_tree_list = kruskals_algorithm.kruskals_algorithm(sorted_list_from_adjecency_list, v)
                    end_time_list = time.time()
                    execution_time_list = end_time_list - start_time_list
                    writer.writerow([v, s, 'list', execution_time_list])


                    start_time_matrix = time.time()
                    minimum_spanning_tree_matrix = kruskals_algorithm.kruskals_algorithm(sorted_list_from_matrix, v)
                    end_time_matrix = time.time()
                    execution_time_matrix = end_time_matrix - start_time_matrix
                    writer.writerow([v, s, 'matrix', execution_time_matrix])


    # for pair in sorted_list_from_adjecency_list:
    #     print(f"{pair[0]} <-> {pair[1]}, weight - {pair[2]}")
    #
    # start_time = time.time()
    # minimum_spanning_tree = kruskals_algorithm.kruskals_algorithm(sorted_list_from_adjecency_list, vertices )
    # end_time = time.time()
    # execution_time = end_time - start_time
    #
    # print("\nMinimum spanning tree:")
    # if len(minimum_spanning_tree) == 0:
    #     print("Sorry, graph is not connected. Minimum spanning tree doesn't exist")
    # else:
    #     for edge in minimum_spanning_tree:
    #         print(f"{edge[0]} <-> {edge[1]}, weight - {edge[2]}")
    #     print(f"Execution time: {execution_time:.6f} seconds")