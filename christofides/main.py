import sys
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(g, plt_ax=None, title=None):
    if plt_ax:
        plt_ax.set_title(title)
    pos = nx.spring_layout(g, seed=125)

    nx.draw_networkx_nodes(g, pos, ax=plt_ax)
    nx.draw_networkx_labels(g, pos, ax=plt_ax)
    if type(g) is nx.MultiGraph:
        for u, v, k in g.edges:
            connectionstyle = f"arc3,rad=0.{1*k}"
            label_pos = 0.5 + 0.1 * k
            if k > 0:
                pos_old = pos
                ax, ay = pos[u]
                bx, by = pos[v]

                lin1 = np.array([[1, ax], [1, bx]])
                lin2 = np.array([ay, by])
                c, d = np.linalg.solve(lin1, lin2)
                new_ay = c + (0.1 * k) + ax * d
                new_by = c + (0.1 * k) + bx * d

            nx.draw_networkx_edges(g, pos, ax=plt_ax, edgelist=[(u, v, k)], connectionstyle=connectionstyle)
            if k > 0:
                pos[u][1] = new_ay
                pos[v][1] = new_by
            nx.draw_networkx_edge_labels(g, pos, edge_labels={(u, v, k): g.get_edge_data(u, v, k)["weight"]},
                                         label_pos=label_pos, ax=plt_ax)
            if k > 0:
                pos = pos_old
    else:
        for u, v in g.edges:
            nx.draw_networkx_edges(g, pos, edgelist=[(u, v)], ax=plt_ax)
            nx.draw_networkx_edge_labels(g, pos, edge_labels={(u, v): g.get_edge_data(u, v)["weight"]}, label_pos=0.6, ax=plt_ax)

nodes = range(1, 6)
g: nx.Graph = nx.complete_graph(nodes, nx.Graph)
nx.set_edge_attributes(g, 1, "weight")
g.edges[4, 2]["weight"] = 2
g.edges[5, 1]["weight"] = 2

weights = nx.get_edge_attributes(g, "weight")
for u, v in g.edges:
    leftovers = set(g.nodes)
    leftovers.remove(u)
    leftovers.remove(v)
    for x in leftovers:
        a = weights.get((u, x)) or weights.get((x, u))
        b = weights.get((v, x)) or weights.get((x, v))
        c = weights.get((u, v)) or weights.get((v, u))
        if not (a + b >= c and a + c >= b and c + b >= a):
            print("graf nie spełnia założeń")
            print("trójkąt: ", u, v, x)
            sys.exit(1)

fig, axes = plt.subplots(2, 2, figsize=(15,10), layout="tight")
axes = np.ravel(axes)
draw_graph(g, axes[0], title="Full graph G")
t: nx.Graph = nx.minimum_spanning_tree(g, "weight")
draw_graph(t, axes[1], title="Minimum spanning tree T")

o = set([i for i, degree in t.degree if degree % 2 == 1])
print("Nodes of odd degree of spanning tree T: ", o)

o_prim = set(g.nodes) - o
g_prim = g.copy()
for node in o_prim:
    g_prim.remove_node(node)
draw_graph(g_prim, axes[2], title="Subgraph G' of G including only nodes from O")
m = nx.min_weight_matching(g_prim)
print("Minimum matching of nodes O in graph G", m)
print("Is perfect matching: ", nx.is_perfect_matching(g_prim, m))
h = nx.MultiGraph()
h.add_nodes_from(nodes)
h.add_weighted_edges_from([(*edge, w) for edge, w in nx.get_edge_attributes(t, "weight").items()])
h.add_weighted_edges_from([(u, v, g.get_edge_data(u, v)["weight"]) for u, v in m])
draw_graph(h, axes[3], title="Eulerian graph H")
initial_tour = list(nx.eulerian_circuit(h, source=1))
tour = [1]
for i, j in initial_tour:
    if j not in tour:
        tour.append(j)
tour.append(tour[0])
tour = [(i, j) for i, j in zip(tour[:-1], tour[1:])]
plt.show()
fig, ax = plt.subplots(1, 1)
fig.clear()
for i, edge in enumerate(tour):
    colors = ["r" if (e[0], e[1]) in tour[:i + 1] or tuple(reversed((e[0], e[1]))) in tour[:i + 1] else "k" for e in
              g.edges]
    pos = nx.spring_layout(g, seed=1)  # Get positions for nodes
    nx.draw_networkx_nodes(g, pos)
    nx.draw_networkx_labels(g, pos)
    nx.draw_networkx_edges(g, pos, edge_color=colors, connectionstyle=["arc3,rad=0.0", "arc3,rad=0.2"])
    nx.draw_networkx_edge_labels(g, pos, edge_labels=nx.get_edge_attributes(g, "weight"))
    name = "{:>2}".format(i).replace(" ", "0")
    plt.savefig(fname=f"graph/{name}.png")