from .FileOperations import FileOperations


class TaskOperations:
    @staticmethod
    def add_task(tasks):
        task = input("Enter a new task: ")
        tasks.append(task)
        FileOperations.update_tasks_file(tasks)

    @staticmethod
    def edit_task(tasks):
        TaskOperations.display_tasks(tasks)
        try:
            task_index = int(input("Enter the number of the task to edit: "))
            old_task = tasks[task_index]
            new_task = input("Enter the new task: ")
            tasks[task_index] = new_task
            print(f"Task updated from '{old_task}' to '{new_task}'")
            FileOperations.update_tasks_file(tasks)
        except (ValueError, IndexError):
            print("Invalid task number")

    @staticmethod
    def remove_task(tasks):
        TaskOperations.display_tasks(tasks)
        try:
            task_index = int(input("Enter the number of the task to remove: "))
            removed_task = tasks.pop(task_index)
            print(f"Task '{removed_task}' removed.")
            FileOperations.update_tasks_file(tasks)
        except (ValueError, IndexError):
            print("Invalid task number")

    @staticmethod
    def complete_task(tasks):
        TaskOperations.display_tasks(tasks)
        try:
            task_index = int(input("Enter the number of the task to mark as complete: "))
            task_to_complete = tasks[task_index]
            if "(complete)" in task_to_complete:
                print(f"Task '{task_to_complete}' is already marked as complete.")
            else:
                tasks[task_index] = task_to_complete + " (complete)"
                print(f"Task '{task_to_complete}' marked as complete.")
                FileOperations.update_tasks_file(tasks)
        except (ValueError, IndexError):
            print("Invalid task number")

    @staticmethod
    def display_tasks(tasks):
        for index, item in enumerate(tasks):
            print(f"{index}: {item}")
