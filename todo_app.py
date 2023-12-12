import json
from datetime import datetime, timedelta

class TodoList:
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename, 'r') as file:
                tasks = json.load(file)
            return tasks
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            return []

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=2)

    def add_task(self, description, priority='medium', due_date=None):
        new_task = {
            'description': description,
            'priority': priority,
            'due_date': due_date.strftime('%Y-%m-%d') if due_date else None,
            'completed': False,
        }
        self.tasks.append(new_task)
        self.save_tasks()

    def remove_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]
            self.save_tasks()
        else:
            print("Invalid task index.")

    def mark_task_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]['completed'] = True
            self.save_tasks()
        else:
            print("Invalid task index.")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return

        print("Task List:")
        for i, task in enumerate(self.tasks):
            status = 'Completed' if task['completed'] else 'Pending'
            print(f"{i + 1}. {task['description']} - Priority: {task['priority']} - Due Date: {task['due_date']} - Status: {status}")

def main():
    todo_list = TodoList()

    while True:
        print("\n1. Add Task\n2. Remove Task\n3. Mark Task as Completed\n4. Display Tasks\n5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            description = input("Enter task description: ")
            priority = input("Enter task priority (high/medium/low): ").lower()
            due_date_str = input("Enter due date (YYYY-MM-DD), press Enter if none: ")
            due_date = datetime.strptime(due_date_str, '%Y-%m-%d') if due_date_str else None
            todo_list.add_task(description, priority, due_date)
            print("Task added successfully.")

        elif choice == '2':
            task_index = int(input("Enter the task index to remove: ")) - 1
            todo_list.remove_task(task_index)
            print("Task removed successfully.")

        elif choice == '3':
            task_index = int(input("Enter the task index to mark as completed: ")) - 1
            todo_list.mark_task_completed(task_index)
            print("Task marked as completed.")

        elif choice == '4':
            todo_list.display_tasks()

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
