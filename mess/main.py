from utility import FileOperations, TaskOperations, UserInterface

"""
main() is the entry point for the todo list CLI application.

It initializes the tasks from file, prints the menu, prompts for user 
input, and calls the appropriate operation functions based on the input.

The main loop continues until the user enters 'quit'.
"""


def main():
    tasks = FileOperations.initialize_tasks()
    while True:
        UserInterface.print_menu()
        action = input().strip().lower()
        if action in "add":
            TaskOperations.add_task(tasks)
        elif action in "show":
            UserInterface.show_tasks(tasks)
        elif action in "edit":
            TaskOperations.edit_task(tasks)
        elif action in "remove":
            TaskOperations.remove_task(tasks)
        elif action in "complete":
            TaskOperations.complete_task(tasks)
        elif action in "quit":
            print("Goodbye!")
            break
        else:
            print("Invalid action")


if __name__ == "__main__":
    main()
