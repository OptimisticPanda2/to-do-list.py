def show_tasks(tasks):
    if not tasks:
        print("\n No tasks to be performed")
    else: 
        print("\n Aapki To-Do List :")
        for i , task in enumerate(tasks,1):
            print(f"{i}.{task}")
            
def main ():
   tasks = []
   while True:
            print("\n============TO-DO-LIST============")
            print("            1. Naya Task Add Karein")
            print("            2. Task Complete Karein(Delete)")
            print("            3. Saare Tasks Dekhein")
            print("            4. Exit Karein")
   choice = input("Apna Option Choose Karein:")
   #task ko add karne ke liye option daale 1 
   if choice == "1":
       task = input("Task Likhein :")
       tasks.appene(task)
       print(f"'{task}' add hogaya!")
    # task ko delete karne ke liye option daale 2
   elif choice =="2":
       show_tasks(tasks)
       try:
           task_no=int(input("Complete Task ka number likhe:"))-1
           if 0<= task_no <= len(tasks):
               removed_task=tasks.pop(task_no) #list se task delete hoga
               print(f"{removed_task} , hataya gaya!")
           else:
               print("Galat task number , Sahi Number Likhein")
       except ValueError:
               print("Valid Number Likho")