# The `add_task_menu` function is part of the To-Do List Application that allows users to add new tasks to their to-do list.
def add_task_menu():
    from main import to_do_list
    task_to_add = input("What task do you want to add?\n")
    to_do_list.append(task_to_add)
    print(f"You've succesfully added {task_to_add} to to_do_list.")
    return 
    


