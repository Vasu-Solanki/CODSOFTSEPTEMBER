# Empty list.
task = [ ]

# Function for adding the task.
def add_task():
    task_name = input("\n->Enter the task you want to add in the list: ").split(", ")
    task.extend(task_name)

    
# Function for shoing the task in the list.
def show_list():
    print(task)
    
    
# Function for delete the task    
def delete():
    n = int(input("->Which task u want to delet: ")) - 1
    print(f"->{task[n]} is deleted!")
    task.remove(task[n])

# Function for exit the the code or loop.
def for_exit():
    
    for_reapeting = False
    

# Variable for repeating the function.   
for_reapeting = True

# Loop for repeating the function.   
while for_reapeting:
    print('''\nMenu:
1)Adding task.
2)Show list.
3)Delete task.
4)Exit. \n''')
    given_task = int(input("-->Enter the no. of task(1/2/3/4): "))

    if given_task <= 4:    
        if given_task == 1:
            add_task()
        
        elif given_task == 2:
            show_list()
            
        elif given_task == 3:
            delete()
            
        elif given_task == 4:
            print("\n->You Exit the list.")
            exit()
            
    elif (given_task < 4) :
        print("-->Please! Enter a valid input<--")
    
        
        
    
    


    