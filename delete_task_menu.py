
def delete_task_menu():
    while True:
        from main import to_do_list
        for index, task in enumerate(to_do_list):
            print(f"{index + 1}. {task.capitalize()}")
        task_to_delete = input(f"Which task would you like to delete?\n").lower()
        try:
            task_to_delete = int(task_to_delete)
            if task_to_delete <= len(to_do_list):
                return to_do_list.remove(to_do_list[task_to_delete - 1])
            else:
                input("You didn't enter a valid number. Try again by pressing 'enter'.\n ")
        except:
            input("You should be inputing a number. Try again by pressing 'enter'.\n ")
        