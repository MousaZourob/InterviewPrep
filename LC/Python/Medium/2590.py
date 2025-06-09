class TodoList:

    def __init__(self):
        self.tasks = {}
        self.users = defaultdict(list)
        self.tags = defaultdict(list)
        self.task_id = 1
        self.farthest_date = 0

    def addTask(self, userId: int, taskDescription: str, dueDate: int, tags: List[str]) -> int:
        self.tasks[self.task_id] = [dueDate, taskDescription, False]
        self.users[userId].append(self.task_id)
        self.tags[self.task_id].extend(tags)
        
        self.task_id += 1
        self.farthest_date = max(self.farthest_date, dueDate)
        return self.task_id - 1

    def getAllTasks(self, userId: int) -> List[str]:
        buckets = [None] * (self.farthest_date + 1)
        user_tasks = self.users[userId]
        todoTasks = []
        
        for task_id in user_tasks:
            task = self.tasks[task_id]
            if not task[2]:
                buckets[task[0]] = task[1]
                    
        return [task for task in buckets if task != None]

    def getTasksForTag(self, userId: int, tag: str) -> List[str]:
        buckets = [None] * (self.farthest_date + 1)
        user_tasks = self.users[userId]
        todoTasks = []
        
        for task_id in user_tasks:
            if tag in self.tags[task_id]:
                task = self.tasks[task_id]
                if not task[2]:
                    buckets[task[0]] = task[1]
                    
        return [task for task in buckets if task != None]

    def completeTask(self, userId: int, taskId: int) -> None:
        user_tasks = self.users[userId]
        if taskId in user_tasks:
            self.tasks[taskId][2] = True


# Your TodoList object will be instantiated and called as such:
# obj = TodoList()
# param_1 = obj.addTask(userId,taskDescription,dueDate,tags)
# param_2 = obj.getAllTasks(userId)
# param_3 = obj.getTasksForTag(userId,tag)
# obj.completeTask(userId,taskId)