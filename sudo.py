Priority_Task = []
Minimal_Task = []
is_running = True
while is_running == True:
 print('1.) Add task ')
 print('2.) View Task')
 print('3.) Exit ')
 choice = input()


 if choice == '1':
  print('1.) Priority task')
  print('2.) Minimal Task')
  Task_type = input()
  print('Task and Deadline')
  TaskName= input()
  if Task_type == '1':
    Priority_Task.append(TaskName + '*')
    print('task added successfully!')

  elif Task_type == '2':
   Minimal_Task.append(TaskName + '-')
   print('task added successfully!')
 elif choice == '2':
   print ('1.) Priority Task')
   print ('2.) Minimal Task')
   view_choice = input()

   if view_choice == '1':
    print ('======Priority Task=======')
    for task in Priority_Task:
     print (task)

   elif view_choice == '2':
     print ("+++++ Minimal Task +++++" )
     for task in Minimal_Task:
      print (task)

 elif choice == '3':
  print('Program sucessfuly ended')
  is_running = False



   



 





      
