# To Do List Application
---
The point of this project was to create a to do list application where you could add, view, delete and quit the application based on the user's input.

## Main_Menu function
This function takes a list of options the user can pick from and prints it in menu form for the user to choose from. The user must type out the correct option. If the user mistypes, inputs a number or leaves the option blank, it calls the test_error function to manage the errors.

## Add_task(s)
This function asks the user_input and adds(appends) the task to the task list. After adding the task to the list, it then prints out a confirmation message to the user.

## View_task(s)
This function prints out a list of the available tasks in the list. If the task list is empty, it will also print out a message to the user.

## Delete_task(s)
This function asks the user what task they would like to remove from the task list. It then checks the task list to see if that task is on the list. If it is then it removes that task, if it is not then it prints an error message to the user.

## Biggest Challenge
The biggest challenge of these functions was implementing the try and except functions. I found myself wanting to use if and Elif and else blocks for my error handling instead. I had to look up serval examples of this method until I found one that made sense to me. Once again overthinking the process.

## What did I learn?
I learned that try and except blocks can be more effective than if, else blocks in some situations. There is nothing better than incorporating new skills to improve and evaluate your skills.



