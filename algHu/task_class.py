class Task:
    name = ""
    depends_on = []
    blocks = []
    level = 0
    
    def __init__(self, name):
        self.name = name
    def add_deps(self, deps: list['Task']):
        self.depends_on = deps
    def add_blocks(self, blocks: list['Task']):
        self.blocks = blocks
    def set_level(self, start):
        res = dfs(start, self, 1)
        self.level = res
    def __str__(self):
        return f"Task(name=\"{self.name}\", level={self.level})"
    def __repr__(self):
        return self.__str__()
    def remove_deps(self: 'Task', task_list: list['Task']):
        for task in task_list:
            if self in task.depends_on:
                task.depends_on.remove(self)

def dfs(current: Task, finish: Task, lv: int) -> int:
    if current.name == finish.name:
        return lv
    elif current.depends_on == []:
        return 0
    else:
        if finish in current.depends_on:
            return lv + 1
        else:
            max_depth = 0
            for dependency in current.depends_on:
                result = dfs(dependency, finish, lv + 1)
                max_depth = result if result > max_depth else max_depth
            return max_depth