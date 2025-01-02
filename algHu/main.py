from task_class import Task
from tree_test import test_in_forest, test_in_tree, test_out_tree, test_out_forest, switch_prec_direction
import hu_alg

M = 3

def main(task_list: list[Task]):
    if test_in_tree(task_list):
        res=hu_alg.hus_alg(3, task_list)
        hu_alg.draw_timetable(res)
        return
    if test_out_tree(task_list):
        in_tree = switch_prec_direction(task_list)
        pass

def create_tasks(order) -> list[Task]:
    tasks_dict={f"z{n}":Task(f"z{n}") for n in range(1, 19)}
    tasks = []
    for t_name, t in tasks_dict.items():
        deps = [tasks_dict[d] for d in order.get(t_name) or []]
        t.add_deps(deps)
        for d in deps:
            d.add_blocks([t])
        tasks.append(t)
    return tasks

def create_tasks_out(order) -> list[Task]:
    tasks_dict={f"z{n}":Task(f"z{n}") for n in range(1, 19)}
    tasks: list[Task] = []
    for t_name, t in tasks_dict.items():
        deps = [tasks_dict[d] for d in order[t_name]]
        t.add_blocks(deps)
        for d in deps:
            d.add_deps([t])
        tasks.append(t)
    for t in tasks:
        t.set_level()
    return tasks

forest = {
    "z1": ["z2", "z3"],
    "z2": ["z4", "z5"],
    "z3": ["z6", "z7"],
    "z4": ["z8"],
    "z5": ["z9"],
    "z6": [],
    "z7": [],
    "z8": [],
    "z9": [],
    "z10": ["z11"],
    "z11": ["z12", "z13"],
    "z12": ["z14", "z15"],
    "z13": ["z16"],
    "z14": [],
    "z15": [],
    "z16": ["z17", "z18"],
    "z17": [],
    "z18": []
}

order_1 = {
    "z1": [],
    "z2": [],
    "z3": [],
    "z4": [],
    "z5": [],
    "z6": [],
    "z7": ["z1", "z2", "z3"],
    "z8": ["z4"],
    "z9": ["z5", "z6"],
    "z10": ["z7"],
    "z11": ["z8", "z9"],
    "z12": ["z10", "z11"]
}

in_tree_1: list[Task] = hu_alg.order_tasks_topographically(create_tasks(order_1)[:12])
in_tree_2: list[Task] = hu_alg.order_tasks_topographically(create_tasks(forest)[:9])

in_forest=create_tasks(forest)
# out_tree=create_tasks(in_order)[:9]
# out_forest=create_tasks_out(in_order)
main(in_tree_1)
