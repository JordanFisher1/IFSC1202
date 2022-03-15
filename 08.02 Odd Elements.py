def splitevenodd(A): 
   evenlist = [] 
   oddlist = [] 
   for i in A: 
      if (i % 2 == 0): 
         evenlist.append(i) 
      else: 
         oddlist.append(i) 
   print("Odd lists:", oddlist) 
  

A=list()
n=int(input("How many Values are there?: "))
for i in range(int(n)):
   k=int(input(""))
   A.append(k)
splitevenodd(A) 