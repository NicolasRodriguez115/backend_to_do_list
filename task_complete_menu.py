# The `task_complete_menu` function is a feature of the To-Do List Application that allows users to mark tasks as completed.
def task_complete_menu():
    while True:
        from main import to_do_list
        for index,task in enumerate(to_do_list):
            print(f"{index + 1}. {task.capitalize()}")
        searched_task = input(f"Which task would you like to mark as complete?\n").lower()
        try:
            searched_task = int(searched_task)
            if searched_task <= len(to_do_list):
                to_do_list[searched_task - 1] = to_do_list[searched_task - 1] + " ✅" 
                return
            else:
                input("You didn't enter a valid number. Try again by pressing 'enter'.\n ")
        except:
            input("You should be inputing a number. Try again by pressing 'enter'.\n ")