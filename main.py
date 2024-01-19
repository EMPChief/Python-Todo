import os
todo = []
filename = "todo.txt"

if not os.path.exists(filename):
    with open(filename, "w") as file:
        pass

with open(filename, "r") as file:
    todo = file.read().splitlines()

while True:
    user_action = input("Type what you want to do: Add, Show, Edit, Remove, q/quit ").strip().lower()
    match user_action:
        case "add":
            new_todo = input("Type your todo: ")
            todo.append(new_todo)
            with open(filename, "a") as file:
                file.write(f"{new_todo}\n")
        case "show":
            for item in todo:
                item = item.title()
                print(f"Todo: {item}")
        case "edit":
            print("Current items:")
            for i, item in enumerate(todo):
                print(f"{i}: {item}")
            number = int(input("Type the number of the item you want to edit: "))
            previous_todo = todo[number]
            new_todo = input("Type your new todo: ")
            todo[number] = new_todo
            print(f"Item {previous_todo} edited. New todo: {new_todo}")
            with open(filename, "w") as file:
                file.write("\n".join(todo))
        case "remove":
            number = int(input("Type the number of the item you want to remove: "))
            del todo[number]
            print(f"Item {number} removed.")
            with open(filename, "w") as file:
                file.write("\n".join(todo))
        case "complete":
            print("Current items:")
            for i, item in enumerate(todo):
                print(f"{i}: {item}")
            number = int(input("Type the number of the item you want to complete: "))
            completed_todo = todo[number]
            del todo[number]
            print(f"Item {completed_todo} completed and removed.")
            with open(filename, "w") as file:
                file.write("\n".join(todo))
        case _:
            if user_action in ['q', 'quit']:
                print("Goodbye!")
                break
            else:
                print("Invalid action")
