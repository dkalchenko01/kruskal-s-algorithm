def convert_adjecency_list_to_sorted_list(adjecency_list):
    tuples_list = []
    for i in range(len(adjecency_list)):
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