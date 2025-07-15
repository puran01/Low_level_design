from enum import Enum
from datetime import datetime

class User:
    def __init__(self, name,id, email):
        self.name = name
        self.id = id
        self.email = email

class TaskStatus(Enum):
    Pending=1
    Progress=2
    Completed=3

class Task:
    def __init__(self,id, title,description, due_date,priority,assigned_user ):
        self.id = id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.assigned_user = assigned_user
        self.status = TaskStatus.Pending
    
class TaskManager:
    _instance = None
    def __init__(self):
        self.Tasks = {}
        self.task_history = []

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
    
    def log_history(self, task_id, action, details=""):
        timestamp = datetime.now().isoformat()
        self.task_history.append({ "task_id": task_id,
            "action": action,
            "timestamp": timestamp,
            "details": details})
    
    def create_task(self,id, title,description, due_date,priority,assigned_user):
        self.Tasks[id] = Task(id=id, title=title, description=description,due_date=due_date,priority=priority,assigned_user=assigned_user)
        self.log_history(id, "Created", f"Assigned to {assigned_user.name}")
        return "Task Added"

    def update_task(self,id, status):
        if id in self.Tasks:
            self.Tasks[id].status = status
            self.log_history(id, "Status Updated", f"New status: {status.name}")
            return "Task Updated"
        return "Task Not found"
    
    def delete_task(self,id):
        if id in self.Tasks:
            del self.Tasks[id]
            self.log_history(id, "Deleted")
            return "Task deleted"
        return "Task not found"
    
    def search_task(self, id, title):
        task = self.Tasks.get(id)
        if task and task.title == title:
            return task
        return None
    
    def mark_task_completed(self,id):
        if id in self.Tasks:
            self.Tasks[id].status = TaskStatus.Completed
            self.log_history(id, "Marked Completed", "Status set to Completed")
            return "Task marked as Completed"
        return "Task not found"

    def filtering_task_by_priority(self, priority):
        t = []
        for task in self.Tasks.values():
            if task.priority == priority:
                t.append(task.title)
        return t

    def filtering_task_by_due_date(self, due_date):
        t = []
        for task in self.Tasks.values():
            if task.due_date == due_date:
                t.append(task.title)
        return t

    def filtering_task_by_assigned_user(self, assigned_user):
        t = []
        for task in self.Tasks.values():
            if task.assigned_user == assigned_user:
                t.append(task.title)
        return t
    
                
if __name__ == "__main__":
    # Create a user
    user1 = User("Alice", 1, "alice@example.com")

    # Get Singleton TaskManager instance
    manager = TaskManager.get_instance()

    # Create tasks
    print(manager.create_task(
        id=101,
        title="Complete Report",
        description="Finish monthly finance report",
        due_date="2025-07-30",
        priority=1,
        assigned_user=user1
    ))

    print(manager.create_task(
        id=102,
        title="Team Meeting",
        description="Prepare agenda for the team meeting",
        due_date="2025-08-05",
        priority=2,
        assigned_user=user1
    ))

    # Update a task status to In Progress
    print(manager.update_task(101, TaskStatus.Progress))

    # Mark a task as completed
    print(manager.mark_task_completed(101))

    # Search for a task
    task = manager.search_task(101, "Complete Report")
    if task:
        print(f"\nFound Task: {task.title}, Status: {task.status.name}, Assigned to: {task.assigned_user.name}")

    # Filtering examples
    print("\nTasks with priority 1:", manager.filtering_task_by_priority(1))
    print("Tasks assigned to Alice:", manager.filtering_task_by_assigned_user(user1))
    print("Tasks due on 2025-08-05:", manager.filtering_task_by_due_date("2025-08-05"))

    # Delete a task
    print(manager.delete_task(102))

    # Print Task History Log
    print("\nTask History Log:")
    for entry in manager.task_history:
        print(entry)
