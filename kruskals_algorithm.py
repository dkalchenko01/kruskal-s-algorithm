from operator import truediv


def convert_adjecency_list_to_sorted_list(adjecency_list: dict):
    tuples_list = []
    for i in adjecency_list.keys():
        for pair in adjecency_list[i]:
            if (pair[0], i, pair[1]) not in tuples_list:
                tuples_list.append((i, pair[0], pair[1]))
    sorted_by_weight = list(sorted(tuples_list, key=lambda x: x[2]))
    return sorted_by_weight

def convert_matrix_to_sorted_list(matrix , n):
    tuples_list = []
    for i in range(n):
        for j in range(n):
            if (matrix[i][j] != None) and (j,i, matrix[i][j]) not in tuples_list:
                tuples_list.append((i,j, matrix[i][j]))
    sorted_by_weight = list(sorted(tuples_list, key=lambda x: x[2]))
    return sorted_by_weight

def kruskals_algorithm(sorted_list, n):
    minimum_spanning_tree = []
    is_added = set()
    for edge in sorted_list:
        if ((edge[0] not in is_added) or (edge[1] not in is_added)) and (not check_cycle(edge[0], edge[1], minimum_spanning_tree)):
            minimum_spanning_tree.append(edge)
            is_added.add(edge[0])
            is_added.add(edge[1])
        if len(minimum_spanning_tree) > n - 1:
            print("Sorry, graph is not connected. minimum spanning tree doesn't exist")
            break
    return minimum_spanning_tree

def check_cycle(v1, v2, tree):
    v1_neighbours = [x[1] for x in tree if x[0] == v1]
    v1_neighbours += [x[0] for x in tree if x[1] == v1]
    if v2 in v1_neighbours:
        return True
    elif len(v1_neighbours) <= 1:
        return False
    else:
        for neighbour in v1_neighbours:
            check_cycle(neighbour, v2, tree)


