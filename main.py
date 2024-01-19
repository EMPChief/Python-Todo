import os
import time
todo = []
filename = "todo.txt"

if not os.path.exists(filename):
    with open(filename, "w") as file:
        pass

with open(filename, "r") as file:
    todo = file.read().splitlines()

while True:
    user_action = input("Type what you want to do:\nAdd\nShow\nEdit\nRemove\nComplete\nq/quit ").strip().lower()

    if user_action == "add":
        new_todo = input("Type your todo: ")
        todo.append(new_todo)
        with open(filename, "a") as file:
            file.write(f"{new_todo}\n")

    elif user_action == "show":
        for item in todo:
            item = item.title()
            print(f"Todo: {item}")
        time.sleep(3)

    elif user_action == "edit":
        print("Current items:")
        for i, item in enumerate(todo):
            print(f"{i}: {item}")
        try:
            number = int(input("Type the number of the item you want to edit: "))
            previous_todo = todo[number]
            new_todo = input("Type your new todo: ")
            todo[number] = new_todo
            print(f"Item {previous_todo} edited. New todo: {new_todo}")
            with open(filename, "w") as file:
                file.write("\n".join(todo))
        except (ValueError, IndexError):
            print("Invalid number")

    elif user_action == "remove":
        try:
            number = int(input("Type the number of the item you want to remove: "))
            del todo[number]
            print(f"Item {number} removed.")
            with open(filename, "w") as file:
                file.write("\n".join(todo))
        except (ValueError, IndexError):
            print("Invalid number")

    elif user_action == "complete":
        print("Current items:")
        for i, item in enumerate(todo):
            print(f"{i}: {item}")
        try:
            number = int(input("Type the number of the item you want to complete: "))
            completed_todo = todo[number]
            del todo[number]
            print(f"Item {completed_todo} completed and removed.")
            with open(filename, "w") as file:
                file.write("\n".join(todo))
        except (ValueError, IndexError):
            print("Invalid number")

    elif user_action in ['q', 'quit']:
        print("Goodbye!")
        break

    else:
        print("Invalid action")
