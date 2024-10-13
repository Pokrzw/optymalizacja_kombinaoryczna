
from pprint import pprint

vertices = ["A", "B", "C", "D"]
edges_mappings = { "A": ["C", "B", "D"], "B": ["A", "C"], "C": ["A", "B"], "D":["A"]}
matrix_size = len(vertices) * len(vertices)
matrix_base = [0] * len(vertices)
index = 0
for v in vertices:
    neighbours = edges_mappings[v]
    mini_matrix = [0] * len(vertices)
    for n in neighbours:
        i = vertices.index(n)
        mini_matrix[i] = 1
    matrix_base[index] = mini_matrix
    index += 1
print(matrix_base)


index = 0
for x in vertices:
    mini_matrix = [0] * len(vertices)
    adj_vertices = edges_mappings[x]
    for adj_vertex in adj_vertices:
        i = vertices.index(adj_vertex)
        mini_matrix[i] = 1
    matrix_base[index] = mini_matrix
    index=+1

pprint(matrix_base)