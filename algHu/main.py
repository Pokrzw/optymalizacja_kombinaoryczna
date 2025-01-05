from task_class import Task
import hu_alg

M = 3

def main(task_list: list[Task]):
    res=hu_alg.hus_alg(M, task_list)
    hu_alg.draw_timetable(res)
    return

def create_tasks(order) -> list[Task]:
    tasks_dict={f"z{n}":Task(f"z{n}") for n in range(1, len(order)+1)}
    tasks = []
    for t_name, t in tasks_dict.items():
        deps = [tasks_dict[d] for d in order.get(t_name) or []]
        t.add_deps(deps)
        for d in deps:
            d.add_blocks([t])
        tasks.append(t)
    last_task = tasks[-1]
    for task in tasks:
        task.set_level(last_task)
    return tasks


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

order_2 = {
    "z1": [],
    "z2": [],
    "z3": [],
    "z4": [],
    "z5": [],
    "z6": [],
    "z7": ["z1", "z2"],
    "z8": ["z3"],
    "z9": ["z5", "z4"],
    "z10": ["z6","z7"],
    "z11": ["z8", "z9"],
    "z12": ["z10", "z11"]
}

in_tree=create_tasks(order_1)
main(in_tree)
