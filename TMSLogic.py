class TMSLogic:
    def __init__(self):
        self.tasks = []

    def add_task(self, task:str):
        self.tasks.append((task, False))

    def delete_tasks(self):
        self.tasks.clear()

    def toggle_task(self, task_idx:int):
        task, done = self.tasks[task_idx]
        self.tasks[task_idx] = (task, not done)

    def completion_rate(self):
        counter = 0
        for task, done in self.tasks:
            if done:
                counter +=1
        return counter / len(self.tasks)
        

if __name__ == "__main__":
    tms = TMSLogic()
    tms.add_task("t1")
    tms.add_task("t2")
    tms.add_task("t3")
    print(tms.tasks)
    print(tms.completion_rate())
    tms.toggle_task(2)
    print(tms.tasks)
    print(tms.completion_rate())


