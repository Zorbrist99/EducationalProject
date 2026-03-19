class Task:
    def __init__(self, title, done=False):
        self.title = title
        self.done = done

    def __repr__(self):
        return f"[Task('{self.title}',{self.done})]"


class TaskManager:
    def __init__(self):
        self.list_tasks = []

    def __repr__(self):
        return ''

    def get_done_tasks(self):
        for value in self.list_tasks:
            if value.done:
                print(value)
        return self

    def add(self, cls: Task):
        self.list_tasks.append(cls)


tm = TaskManager()
tm.add(Task("do homework"))
tm.add(Task("read", True))
print(tm.get_done_tasks())  # [Task("read", True)]
