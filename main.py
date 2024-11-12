# main.py

import json
from datetime import datetime

class Task:
    def __init__(self, title, description='', due_date=None, priority='Medium'):
        """Initializes a task with basic details."""
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.status = 'Pending'
    
    def mark_as_completed(self):
        """Marks the task as completed."""
        self.status = 'Completed'
    
    def to_dict(self):
        """Converts task data to a dictionary for JSON storage."""
        return {
            'title': self.title,
            'description': self.description,
            'due_date': self.due_date,
            'priority': self.priority,
            'status': self.status
        }
    
    @classmethod
    def from_dict(cls, data):
        """Creates a Task instance from a dictionary."""
        task = cls(
            data['title'],
            data['description'],
            data['due_date'],
            data['priority']
        )
        task.status = data['status']
        return task

class ToDoListManager:
    def __init__(self):
        """Initializes an empty list of tasks."""
        self.tasks = []
    
    def add_task(self, title, description='', due_date=None, priority='Medium'):
        task = Task(title, description, due_date, priority)
        self.tasks.append(task)
    
    def list_tasks(self):
        """Lists all tasks in the to-do list."""
        if not self.tasks:
            print("No tasks to display.")
        for idx, task in enumerate(self.tasks, start=1):
            print(f"{idx}. {task.title} - {task.status} (Priority: {task.priority})")
            if task.due_date:
                print(f"   Due Date: {task.due_date}")
            if task.description:
                print(f"   Description: {task.description}")
    
    def mark_task_completed(self, index):
        """Marks a task as completed given its index in the list."""
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_as_completed()
            print(f"Task '{self.tasks[index].title}' marked as completed.")
        else:
            print("Invalid task index.")
    
    def delete_task(self, index):
        """Deletes a task given its index in the list."""
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            print(f"Task '{removed_task.title}' deleted.")
        else:
            print("Invalid task index.")
    
    def save_to_file(self, filename='tasks.json'):
        """Saves all tasks to a JSON file."""
        with open(filename, 'w') as file:
            tasks_data = [task.to_dict() for task in self.tasks]
            json.dump(tasks_data, file, indent=4)
        print("Tasks saved to file.")
    
    def load_from_file(self, filename='tasks.json'):
        """Loads tasks from a JSON file."""
        try:
            with open(filename, 'r') as file:
                tasks_data = json.load(file)
                self.tasks = [Task.from_dict(data) for data in tasks_data]
            print("Tasks loaded from file.")
        except FileNotFoundError:
            print("No saved tasks found.")

def display_menu():
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Save Tasks to File")
    print("6. Load Tasks from File")
    print("7. Exit")

def main():
    manager = ToDoListManager()
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description (optional): ")
            due_date = input("Enter due date (optional, format YYYY-MM-DD): ")
            priority = input("Enter priority (Low, Medium, High): ")
            manager.add_task(title, description, due_date, priority)
            print("Task added.")
        
        elif choice == '2':
            manager.list_tasks()
        
        elif choice == '3':
            index = int(input("Enter task index to mark as completed: ")) - 1
            manager.mark_task_completed(index)
        
        elif choice == '4':
            index = int(input("Enter task index to delete: ")) - 1
            manager.delete_task(index)
        
        elif choice == '5':
            filename = input("Enter filename to save tasks (default: tasks.json): ")
            if not filename:
                filename = 'tasks.json'
            manager.save_to_file(filename)
        
        elif choice == '6':
            filename = input("Enter filename to load tasks (default: tasks.json): ")
            if not filename:
                filename = 'tasks.json'
            manager.load_from_file(filename)
        
        elif choice == '7':
            print("Exiting the application.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
