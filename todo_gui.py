import tkinter as tk
from tkinter import simpledialog, messagebox, PhotoImage
import datetime
import os
import json
from pathlib import Path

class FileOperations:
    db_folder = Path("db")
    filename = db_folder / "db.json"

    @staticmethod
    def initialize_tasks():
        FileOperations.db_folder.mkdir(parents=True, exist_ok=True)

        if not FileOperations.filename.exists():
            with FileOperations.filename.open("w") as file:
                json.dump([], file, indent=4)
            return []

        with FileOperations.filename.open("r") as file:
            return json.load(file)

    @staticmethod
    def update_tasks_file(tasks):
        with FileOperations.filename.open("w") as file:
            json.dump(tasks, file, indent=4)
            
class TodoApp:
    def __init__(self, root):
        self.root = root
        root.title("Todo List")
        logo_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bmklogo1.png")
        self.logo = PhotoImage(file=logo_path)
        root.iconphoto(False, self.logo)

        try:
            icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "favicon.ico")
            root.iconbitmap(icon_path)
        except Exception as e:
            print(f"Error setting icon: {e}")

        bg_color = "#333333"
        fg_color = "#FFFFFF"
        text_bg_color = "#1E1E1E"

        root.configure(bg=bg_color)

        self.text_area = tk.Text(root, height=20, width=60, bg=text_bg_color, fg=fg_color)
        self.text_area.pack()

        add_button = tk.Button(root, text="Add Task", command=self.add_task, bg=bg_color, fg=fg_color)
        add_button.pack()

        show_button = tk.Button(root, text="Show Tasks", command=self.show_tasks, bg=bg_color, fg=fg_color)
        show_button.pack()

        edit_button = tk.Button(root, text="Edit Task", command=self.edit_task, bg=bg_color, fg=fg_color)
        edit_button.pack()

        remove_button = tk.Button(root, text="Remove Task", command=self.remove_task, bg=bg_color, fg=fg_color)
        remove_button.pack()

        complete_button = tk.Button(root, text="Complete Task", command=self.complete_task, bg=bg_color, fg=fg_color)
        complete_button.pack()

        self.tasks = FileOperations.initialize_tasks()
        self.show_tasks()

    def add_task(self):
        task_description = simpledialog.askstring("Add Task", "Enter a new task:", parent=self.root)
        if task_description:
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            new_task = {
                "description": task_description,
                "status": "ongoing",
                "created_at": current_time
            }
            self.tasks.append(new_task)
            FileOperations.update_tasks_file(self.tasks)
            self.show_tasks()

    def show_tasks(self):
        self.text_area.delete('1.0', tk.END)
        for index, task in enumerate(self.tasks):
            self.text_area.insert(tk.END, f"{index}: {task['description']} | Status: {task['status']}\n")

    def edit_task(self):
        task_index = simpledialog.askinteger("Edit Task", "Enter the number of the task to edit:", parent=self.root)
        if task_index is not None and 0 <= task_index < len(self.tasks):
            new_task_description = simpledialog.askstring("Edit Task", "Enter the new task description:", parent=self.root)
            if new_task_description:
                old_task_description = self.tasks[task_index]["description"]
                self.tasks[task_index]["description"] = new_task_description
                FileOperations.update_tasks_file(self.tasks)
                messagebox.showinfo("Task Updated", f"Task updated from '{old_task_description}' to '{new_task_description}'")
                self.show_tasks()
            else:
                messagebox.showwarning("No Change", "No new description provided.")
        else:
            messagebox.showerror("Error", "Invalid task number")

    def remove_task(self):
        task_index = simpledialog.askinteger("Remove Task", "Enter the number of the task to remove:", parent=self.root)
        if task_index is not None and 0 <= task_index < len(self.tasks):
            removed_task = self.tasks.pop(task_index)
            FileOperations.update_tasks_file(self.tasks)
            messagebox.showinfo("Task Removed", f"Task '{removed_task['description']}' removed.")
            self.show_tasks()
        else:
            messagebox.showerror("Error", "Invalid task number")

    def complete_task(self):
        task_index = simpledialog.askinteger("Complete Task", "Enter the number of the task to mark as complete:", parent=self.root)
        if task_index is not None and 0 <= task_index < len(self.tasks):
            task_to_complete = self.tasks[task_index]
            if task_to_complete["status"] == "complete":
                messagebox.showinfo("Already Complete", f"Task '{task_to_complete['description']}' is already marked as complete.")
            else:
                task_to_complete["status"] = "complete"
                FileOperations.update_tasks_file(self.tasks)
                messagebox.showinfo("Task Completed", f"Task '{task_to_complete['description']}' marked as complete.")
                self.show_tasks()
        else:
            messagebox.showerror("Error", "Invalid task number")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
