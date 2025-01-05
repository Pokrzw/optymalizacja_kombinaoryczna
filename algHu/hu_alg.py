import os
import shutil
import task_class as tc
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def draw_graph(filtered_list:[tc.Task], all_nodes_list: [tc.Task], i: int, half: int): # type: ignore
    g = nx.DiGraph()
    for t in all_nodes_list:
        if t in filtered_list:
            g.add_node(t.name, node_color='red')
        else:
            g.add_node(t.name)
    for t in all_nodes_list:
        for d in t.depends_on:
            g.add_edge(d.name, t.name)
    import matplotlib.pyplot as plt

    pos = nx.drawing.nx_pydot.graphviz_layout(g, "dot")
    plt.close()
    nx.draw(g, pos=pos, with_labels=True)
    nx.draw_networkx_nodes(g, pos=pos, node_color=[vals.get("node_color") or "teal" for _, vals in g.nodes.data()])
    plt.savefig(f"steps/tree{i}-{half}.png")

def draw_timetable(tt: list[list[tuple[int, tc.Task]]]):
    plt.close()
    import pprint
    pprint.pprint(tt)
    tt = list(reversed(tt))
    y_ticks = np.arange(len(tt), 0, step=-1)
    plt.ylim((0, len(tt)))
    plt.yticks(y_ticks, [f"M{i}" for i in reversed(y_ticks)])
    longest_machine = max([len(line) for line in tt])
    turn = 1
    while turn != longest_machine+1:
        widths = []
        lefts = []
        labels = []
        heights = []
        for m in range(len(tt)):
            try:
                task = next(t[1] for t in tt[m] if t[0] == turn)
                widths.append(1),
                lefts.append(turn)
                labels.append(task.name)
                heights.append(m)
            except StopIteration:
                widths.append(0)
                lefts.append(turn)
                heights.append(m)
                labels.append("")
        turn += 1
        bars = plt.barh(list(range(len((tt)))), widths, 1.0, lefts, align="edge", edgecolor="k", linewidth=1)
        plt.bar_label(bars, labels=labels, c="w", label_type="center",  padding=1)
    plt.savefig(f"timetable.png")
    plt.close()


#funkcja do filtra
def filter_func(t: list[tc.Task], cur_max: int):
    res=[]
    for task in t:
        if task.level == cur_max:
            res.append(task)
    return res

def zero_deps(task_list: list[tc.Task]) -> list[tc.Task]:
    res = []
    for task in task_list:
        if len(task.depends_on)==0:
            res.append(task)
    return res
def current_max(task_list: list[tc.Task]) -> int:
    max=0
    for task in task_list:
        if task.level > max:
            max=task.level
    return max

def hus_alg(machines: int, task_list: list[tc.Task]) -> list[list[tc.Task]]:
    #deklarowana ilosc maszyn
    m=machines
    all_machines = []
    for i in range(0, m):
        all_machines.append([])

    #1. t:=1
    t = 1

    if os.path.exists("steps"):
        shutil.rmtree("steps")
    os.mkdir("steps")
    #2. Szeregowanie zadan
    while task_list:
        half = 1
        # Wyznacz liste Lt zadan wolnych w chwili t
        cur_max = current_max(task_list)
        free_tasks = zero_deps(task_list)
        # Lt = filter_func(task_list, cur_max)
        Lt = free_tasks

        to_draw_array: list[tc.Task] = []
        fin = m
        if len(Lt) < m:
            fin = len(Lt)

        for i in range(0,fin):
            element: tc.Task= Lt[i]
            cur_tuple = (t, element)
            to_draw_array.append(element)
        draw_graph(to_draw_array, task_list, t, half)
        
        for i in range(0, fin):
            element: tc.Task= Lt[i]
            cur_tuple = (t, element)
            task_list.remove(element)
            all_machines[i].append(cur_tuple)
        
        for task in to_draw_array:
            task.remove_deps(task_list)
        
        half = 2
        draw_graph(to_draw_array, task_list, t, half)
        t+=1
        
    return all_machines