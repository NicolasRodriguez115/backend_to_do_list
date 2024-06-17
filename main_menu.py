# The `menu` function is the core of the To-Do List Application's user interface. It provides a command-line menu system that allows users to interact with the application.
def menu():
    import os
    from add_task_menu import add_task_menu
    from view_tasks_menu import view_task_menu
    from task_complete_menu import task_complete_menu
    from delete_task_menu import delete_task_menu    
    while True:
        os.system("cls")
        print("""
        Welcome to the To-Do to_do_list App!
        Menu:
        1. Add a task
        2. View tasks
        3. Mark a task as complete
        4. Delete a task
        5. Quit
            """)
        user_input = input("")
        if user_input == "1":
            os.system("cls")
            add_task_menu()
        elif user_input == "2":
            os.system("cls")
            view_task_menu()
        elif user_input == "3":
            os.system("cls")
            task_complete_menu()
        elif user_input == "4":
            os.system("cls")
            delete_task_menu()
        elif user_input == "5":
            break
        else:
            os.system("cls")
            input("Please enter a number from 1 to 5. To try again press 'enter'\n ")
    



