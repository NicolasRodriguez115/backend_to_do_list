#  To-Do List Application

  

This simple Python application allows users to manage a to-do list. The application starts by displaying a main menu where users can choose to add, view, or delete tasks.

  

##  Global Variables

  

-  `to_do_list`: A list that stores the tasks of the to-do list.

  

##  Main Function

  

The `main()` function serves as the entry point of the application.

  

###  Code


```python
to_do_list =  []
def main():
	from main_menu import menu
menu()
if  __name__  ==  "__main__":
	main()
```

### Description

-   At the beginning of the  `main()`  function, it imports the  `menu`  function from the  `main_menu`  module.
-   The  `menu`  function is then called to display the main menu to the user.
-   The  `if __name__ == "__main__":`  block checks if the script is being run directly (not imported as a module). If true, it calls the  `main()`  function to start the application.

# Menu Function Documentation

The `menu` function is the core of the To-Do List Application's user interface. It provides a command-line menu system that allows users to interact with the application.

## Function Definition

```python
def menu():
    import os
    from add_task_menu import add_task_menu
    from view_tasks_menu import view_task_menu
    from task_complete_menu import task_complete_menu
    from delete_task_menu import delete_task_menu    
    while True:
        os.system("cls")
        print("""
        Welcome to the To-Do List App!
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
```
## Description

-   The function starts by importing the necessary modules and functions that handle different tasks within the application.
-   It enters an infinite loop to continuously display the menu until the user decides to exit (`Quit`  option).
-   The  `os.system("cls")`  call clears the console screen to keep the interface clean.
-   The menu presents the user with five options, each corresponding to a specific action within the application:
    1.  **Add a task**: Calls the  `add_task_menu`  function to add a new task.
    2.  **View tasks**: Calls the  `view_task_menu`  function to display current tasks.
    3.  **Mark a task as complete**: Calls the  `task_complete_menu`  function to mark tasks as completed.
    4.  **Delete a task**: Calls the  `delete_task_menu`  function to remove tasks from the list.
    5.  **Quit**: Exits the menu loop and ends the application.
-   If the user enters an invalid option, the function prompts them to try again.

# Add Task Menu Function Documentation

The `add_task_menu` function is part of the To-Do List Application that allows users to add new tasks to their to-do list.

## Function Definition

```python
def add_task_menu():
    from main import to_do_list
    task_to_add = input("What task do you want to add?\n")
    to_do_list.append(task_to_add)
    print(f"You've successfully added {task_to_add} to the to-do list.")
    return
```
## Description

-   The function begins by importing the  `to_do_list`  global variable from the  `main`  module.
-   It prompts the user to enter the task they wish to add to the list.
-   The entered task is then appended to the  `to_do_list`.
-   A confirmation message is printed to inform the user that the task has been successfully added.
-   The function then returns, concluding its execution.

# View Task Menu Function Documentation

The `view_task_menu` function is a component of the To-Do List Application that displays the current list of tasks to the user.

## Function Definition

```python
def view_task_menu():
    from main import to_do_list
    for task in to_do_list:
        print(f"- {task.capitalize()}")
    return input("Press 'enter' to go back.\n ")
```
## Description

-   The function imports the  `to_do_list`  global variable from the  `main`  module.
-   It iterates over each task in the  `to_do_list`  and prints it out, capitalizing the first letter of each task for better readability.
-   After listing all tasks, it prompts the user to press ‘enter’ to return to the main menu.

# Task Complete Menu Function Documentation

The `task_complete_menu` function is a feature of the To-Do List Application that allows users to mark tasks as completed.

## Function Definition

```python
def task_complete_menu():
    while True:
        from main import to_do_list
        for index, task in enumerate(to_do_list):
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
```
## Description

-   The function imports the  `to_do_list`  global variable from the  `main`  module.
-   It enters a loop that continuously displays the tasks and prompts the user to select one to mark as complete.
-   Tasks are displayed with an index number for easy selection.
-   The user is asked to input the number corresponding to the task they wish to mark as complete.
-   If the input is a valid number and within the range of the task list, the selected task is marked with a checkmark (✅) to indicate completion.
-   The function handles invalid inputs by prompting the user to try again.

# Delete Task Menu Function Documentation

The `delete_task_menu` function is part of the To-Do List Application that enables users to remove tasks from their to-do list.

## Function Definition

```python
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
```
## Description

-   The function imports the  `to_do_list`  global variable from the  `main`  module.
-   It enters a loop that continuously displays the tasks with their index numbers and prompts the user to select one to delete.
-   The user is asked to input the number corresponding to the task they wish to delete.
-   If the input is a valid number and within the range of the task list, the selected task is removed from the  `to_do_list`.
-   The function handles invalid inputs by prompting the user to try again.