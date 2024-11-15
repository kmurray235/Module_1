#To do application
#Program can be started with either an empty list or a full one
#new_tasks =["Walk the dog","Water the plants","Feed the fish"]

#Starting program with an empty list
new_tasks =[]

#Adds a task to the new_task list
def add_task():  
  user_input = input("What task would you like to add? ")
  new_tasks.append(user_input)
  print("Your new task "+ user_input +" has been added!")
  print("\n")
  main_menu()

#Views the task(s) in the list
def view_task():  
  print("\n")

  #if the new_task list is empty, else print new_task list
  try:
   if len(new_tasks) == 0:
    print("The task list is empty!\n") 
  except Exception:
    print(f"An exception has occurred:")
    main_menu()
  else:
    for task in new_tasks:    
     print(task + "\n")    
    print("\n")
    main_menu()

#Deletes a specified task from new_task
def delete_task():
  user_input = input("Which task would you like to delete? ")
  
  #if the task is in the list, remove it. Otherwise print error message
  if user_input in new_tasks:
   new_tasks.remove(user_input)
   print ("Removed " + user_input + " from the list of tasks")
   main_menu()
  else: 
    print(user_input + " is not in the list!" + "\n") 
    main_menu()

    
#Creating list of choices for user
def main_menu(): 
 choices = ["Add task(s)","View task(s)","Delete task(s)","Quit the application"]
 
 #prints th elist of choices in the list
 for choice in choices:
    print(choice + "\n")
    
 #User spells out which task they would like to select   
 user_input = input("Please select an option: ")
 
 if user_input == 'Add task(s)':
    add_task()   
 elif user_input == 'View task(s)':
    view_task()
 elif user_input == 'Delete task(s)':
    delete_task() 
 elif user_input == 'Quit the application':
    print("\n")
    print('Goodbye\n')
    exit()
 else:
   #if option is not in list run user_input through test_error function 
   test_error(user_input)

#tests the errors thrown but user_input
def test_error(user_input):
   #is the user_input a number?   
   try:
    user_input == input.isdigit()
   except AttributeError:
        print('Your choice was invaild, try again')
        print('\n')
   
   #is the user_input an empty string?
   try:
    user_input == ''
   except Exception:
      print('Option can not be left blank')
   #No matter what the error, it returns back to the main_menu   
   finally:
      main_menu()
 
 
#Calls the main_menu function
main_menu()



