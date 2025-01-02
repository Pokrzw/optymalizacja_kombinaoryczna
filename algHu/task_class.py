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
    def set_level(self):
        res = dfs(z12, self, 1)
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

#declare tasks
z1 = Task("z1")
z2 = Task("z2")
z3 = Task("z3")
z4 = Task("z4")
z5 = Task("z5")
z6 = Task("z6")
z7 = Task("z7")
z8 = Task("z8")
z9 = Task("z9")
z10 = Task("z10")
z11 = Task("z11")
z12 = Task("z12")

all_tasks = [z1, z2, z3, z4, z5, z6, z7, z8, z9, z10, z11, z12]

#add deps and blocks
z1.add_deps([])
z1.add_blocks([z7])

z2.add_deps([])
z2.add_blocks([z7])

z3.add_deps([])
z3.add_blocks([z7])
#===================
z4.add_deps([])
z4.add_blocks([z8])
#===================
z5.add_deps([])
z5.add_blocks([z9])

z6.add_deps([])
z6.add_blocks([z9])
#===================
#===================
z7.add_deps([z1, z2, z3])
z7.add_blocks([z10])

z8.add_deps([z4])
z8.add_blocks([z11])

z9.add_deps([z5, z6])
z9.add_blocks([z11])
#============
z10.add_deps([z7])
z10.add_blocks([z12])

z11.add_deps([z8, z9])
z11.add_blocks([z12])
#==============
z12.add_deps([z10, z11])
z12.add_blocks([])

# for t in all_tasks:
#     t.set_level()


# pprint.pprint(all_tasks)