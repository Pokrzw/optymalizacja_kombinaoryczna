from task_class import Task
def has_cycle(start: Task) -> bool:
    queue: list[Task] = []
    visited: set[str] = set()

    queue.append(start)
    visited.add(start.name)

    while queue:
        t = queue.pop(0)
        visited.add(t.name)
        neighbours = t.blocks
        if any([n.name in visited for n in neighbours]):
            return True
        queue.extend(neighbours)
    
    return False

def has_cycle_out(start: Task) -> bool:
    queue: list[Task] = []
    visited: set[str] = set()

    queue.append(start)
    visited.add(start.name)

    while queue:
        t = queue.pop(0)
        visited.add(t.name)
        neighbours = t.depends_on
        if any([n.name in visited for n in neighbours]):
            return True
        queue.extend(neighbours)
    
    return False

def path_exists(start: Task, finish: Task) -> bool:
    queue: list[Task] = []
    visited: set[str] = set()

    queue.append(start)

    while queue:
        t = queue.pop(0)
        visited.add(t.name)
        if (t is finish):
            return True
        queue.extend(t.blocks)
        
    return False
    
def test_in_tree(task_list: list[Task]) -> bool:
    roots = [t for t in task_list if not t.blocks]
    if len(roots) > 1 or not roots:
        print(roots)
        print("More than one root")
        return False
    task_produces_cycle = [has_cycle(t) for t in task_list]
    if any(task_produces_cycle):
        print("Produces cycles")
        return False
    root = roots[0]
    leaves = [t for t in task_list if not t.depends_on]
    leaves_connect_to_root = [path_exists(t, root) for t in leaves]
    if not all(leaves_connect_to_root):
        print("Not all leaves have path to root")
        return False
    tasks_have_only_one_child = [len(t.blocks) <= 1 for t in task_list]
    if not all(tasks_have_only_one_child):
        print("Some tasks have more than one child")
        return False
    return True

def test_out_tree(task_list: list[Task]) -> bool:
    roots = [t for t in task_list if not t.depends_on]
    if len(roots) > 1 or not roots:
        return False
    task_produces_cycle = [has_cycle_out(t) for t in task_list]
    if any(task_produces_cycle):
        return False
    root = roots[0]
    leaves = [t for t in task_list if not t.depends_on]
    root_connects_to_leaves = [path_exists(root, t) for t in leaves]
    if not all(root_connects_to_leaves):
        return False
    tasks_have_only_one_parent = [len(t.depends_on) <= 1 for t in task_list]
    if not all(tasks_have_only_one_parent):
        return False

def switch_prec_direction(task_list: list[Task]) -> list[Task]:
    for task in task_list:
        task.depends_on, task.blocks = task.blocks, task.depends_on

def connect_in_forest(task_list: list[Task]) -> list[Task]:
    roots = [t for t in task_list if not t.blocks]
    new_root = Task("temp_root")
    new_root.add_deps(roots)
    for r in roots:
        r.blocks.append(new_root)
    return [new_root, *task_list]

def disconnect_in_forest(task_list: list[Task]) -> list[Task]:
    roots = [t for t in task_list if not t.blocks]
    if len(roots) > 1:
        raise Exception("Not a tree")
    root = roots[0]
    for d in root.depends_on:
        d.blocks=[]
    root.depends_on=[]
    del root
    return [t for t in task_list if t is not root]

def collect_tasks_in(start: Task) -> list[Task]:
    queue: list[Task] = list()
    visisted: set[Task] = set()

    queue.append(start)
    
    while queue:
        t = queue.pop(0)
        visisted.add(t)
        queue.extend([n for n in t.depends_on if n not in visisted])

    return list(visisted)

def collect_tasks_out(start: Task) -> list[Task]:
    queue: list[Task] = list()
    visisted: set[Task] = set()

    queue.append(start)
    
    while queue:
        t = queue.pop(0)
        visisted.add(t)
        queue.extend([n for n in t.blocks if n not in visisted])
    
    return list(visisted)


def test_in_forest(task_list: list[Task]) -> bool:
    roots = [t for t in task_list if not t.blocks]
    trees = [collect_tasks_in(r) for r in roots]
    are_in_tree = [test_in_tree(t) for t in trees]

    if not all(are_in_tree):
        return False
    return True

def test_out_forest(task_list: list[Task]) -> bool:
    roots = [t for t in task_list if not t.depends_on]
    trees = [collect_tasks_out(t) for t in roots]
    are_out_tree = [test_out_tree(t) for t in trees]

    if not all(are_out_tree):
        return False
    return True