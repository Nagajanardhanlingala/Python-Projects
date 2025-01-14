def task():
  tasks = []
  print("WELCOME TO TO DO LIST")

  total_task = int(input("ENTER NO.OF TASKS TO ADD 5="))
  for i in range(1, total_task+1):
    task_name = input(f"Enter task{i} =")
    tasks.append(task_name)

  print(f"Today's tasks are\n{tasks}")
  while True:
    operation = int(input("Enter 1-Add Task\n2-Update Tasks\n3-Delete Tasks\n4-View Tasks\n5-ExitApp/Stop/"))
    if operation == 1:
      add = input("Enter task to add=")
      tasks.append(add)
      print(f"Task successfully Added...")

    elif operation == 2:
      updated_value = input("Enter task to update=")
      if updated_value in tasks:
        up = input("Enter new task=")
        ind = tasks.index(updated_value)
        tasks[ind] = up
        print(f"Task successfully Updated...")
      
    elif operation == 3:
         delete_value = input("Enter task to be deleted= ")
         if delete_value in tasks:
             ind = tasks.index(delete_value)
             del tasks[ind]
             print(f"Task has been Deleted!!")
             
    elif operation == 4:
        print(f"Total Tasks in the list = {tasks}")
        
    elif operation ==5:
        print("Exiting the App.....")
        break
    
    else:
        print("Invalid response!!!")

if __name__ == "__main__":
    task()
