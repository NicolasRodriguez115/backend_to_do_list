
def view_task_menu():

    from main import to_do_list
    for task in to_do_list:
        print(f"- {task.capitalize()}")
    return input("Press 'enter' to go back.\n ")