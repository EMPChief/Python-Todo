todo = []

while True:
    user_action = input("Type what you want to do: Add, Show, Edit, Remove, q/quit ").strip().lower()
    match user_action:
        case "add":
            todo.append(input("Type your todo: "))
        case "show":
            for item in todo:
                item = item.title()
                print(item)
        case "edit":
            number = int(input("Type the number of the item you want to edit: "))
            todo[number] = input("Type your new todo: ")
            print("Item edited", todo)
        case "remove":
            number = int(input("Type the number of the item you want to remove: "))
            del todo[number]
            print("Item removed", todo)
        case _:
            if user_action in ['q', 'quit']:
                print("Goodbye!")
                break
            else:
                print("Invalid action")
