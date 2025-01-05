import networkx as nx
import matplotlib.pyplot as plt
from networkx.classes import path_weight
import os, shutil


def read_from_file(filename, graph):
    with open(filename, "r") as f:
        lines = f.readlines()
        for line in lines:
            a, w, b = line.rstrip("\n").split(" ")
            graph.add_node(a)
            graph.add_node(b)
            graph.add_edge(a,b, weight=int(w))

def chinese_postman(g):
    if nx.is_eulerian(g):
        return list(nx.eulerian_circuit(g))
    if nx.is_semieulerian(g):
        eulerian_path = list(nx.eulerian_path(g))
        start = eulerian_path[0][0]
        end = eulerian_path[-1][-1]
        
        #domyslnie dikstra
        shortest_path_back = nx.shortest_path(g, end, start, weight='weight')
        shortest_path_back = [(i, j) for i, j in zip(shortest_path_back[:-1], shortest_path_back[1:])]
        
        
        eulerian_path.extend(shortest_path_back)
        return eulerian_path
        
    odd_degree_vertices = [i for i, j in g.degree if j % 2 == 1]
    g_prim: nx.Graph = nx.complete_graph(odd_degree_vertices)
    distances = {}
    for edge in g_prim.edges:
        path = nx.shortest_path(g, edge[0], edge[1], weight="weight")
        distance = path_weight(g, path, "weight")
        distances[edge] = distance
        nx.set_edge_attributes(g_prim, distances, "weight")

    matching = nx.min_weight_matching(g_prim, "weight")
    for edge in matching:
        g.add_edge(*edge, weight=nx.path_weight(g_prim, edge, weight="weight"))
    return list(nx.eulerian_circuit(g))

g = nx.MultiGraph()
read_from_file("eulerian", g)
path = chinese_postman(g)

def draw_path_steps(g, path):
    for i, edge in enumerate(path):
        colors = ["r" if (e[0], e[1]) in path[:i+1] or tuple(reversed((e[0], e[1]))) in path[:i+1] else "k" for e in g.edges ]
        pos = nx.spring_layout(g, seed=1)  # Get positions for nodes
        nx.draw_networkx_nodes(g, pos)
        nx.draw_networkx_labels(g, pos)
        nx.draw_networkx_edges(g, pos, edge_color=colors, connectionstyle=["arc3,rad=0.0", "arc3,rad=0.2"])
        nx.draw_networkx_edge_labels(g, pos, edge_labels=nx.get_edge_attributes(g, "weight"))
        name = "{:>2}".format(i).replace(" ", "0")
        plt.savefig(fname=f"graph/{name}.png")

folder = './graph'
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))

draw_path_steps(g, path)
