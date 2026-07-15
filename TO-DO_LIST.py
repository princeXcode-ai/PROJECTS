print("===================")
print("    TO-DO LIST")
print("===================\n")

tasks = []

while True:
    print("Press 1 for add task")
    print("Press 2 for view tasks")
    print("Press 3 for update task")
    print("Press 4 for remove task\n")

    check = int(input("Enter :- "))
    
    def add_task():
        user = input("Add task :-").strip()
        
        if user== "":
            print("No task added")
            
        else:
            tasks.append(user)
            print("\nTask successfully add")
            
        
    def view_task():
        if len(tasks)== 0:
            print("NO task available")
            return
        else:
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")
        
    def update_task():
        if len(tasks)== 0:
            print("NO task available")
            return
        else:
            print(view_task())
            user_1 = int(input("Enter task number to update :- "))
            
            if 1 <= user_1 <= len(tasks):
                new_task = input("Enter new task :- ")
                tasks[user_1-1]= new_task
            
                print("\nTask updated successfully")
            else:
                print("No that much task is available")
                
        
    def delete_file():
        if len(tasks)== 0:
            print("NO task available")
            return
        else:
            print(view_task())
            user_2 = int(input("Enter task number to Remove :- "))
            
            if 1 <= user_2 <= len(tasks):
                tasks.pop(user_2-1)
                print("Task Removed successfully")
            else:
                print("No much task is available")
                
            
            
    if check == 1:
        add_task()
        
    if check == 2:
        view_task()
    
    if check == 3:
        update_task()  
        
    if check == 4:
        delete_file()
        
    user_l =input("do you want to do again [yes/no]:- ").lower() .strip()
    
    if user_l == "yes":
        continue

    elif user_l== "no":
        print("THANKS for using TO-DO List")
        break
    else:
        print("Invalid input! please enter only 'yes' or 'no'.")
                




    