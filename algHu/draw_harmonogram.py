import task_class as tc
import networkx as nx
import matplotlib.pyplot as plt
import hu_alg as hu

def machine_graph(machine_list: list[list[tuple[int, tc.Task]]]):
    fig, axes = plt.subplots(1, 2, squeeze=True, figsize=(15, 5), width_ratios=[1, 2])
    plt.sca(axes[1])
    line_times = []
    for i in range(0, len(machine_list)):
        line_times.append(0)
    ticks_to_set = []
    for i in range(0, len(machine_list)):
        ticks_to_set.append(i)
    axes[1].yaxis.set_ticks(ticks_to_set)
    for i in range(len(machine_list)):
        y = []
        labels = []
        bars = []
        lefts = []
        for j in range(len(machine_list[i])):
            pass

machine_graph(hu.all_machines)