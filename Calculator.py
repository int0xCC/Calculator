def add(X, Y):    
   return X + Y
   
def sub(X, Y):   
   return X - Y
   
def mul(X, Y):   
   return X * Y
   
def div(X, Y): 
   return X / Y    
   
print ("What operation would you like to perform?")    
print ("a.Addition")    
print ("b.Subtraction")    
print ("c.Multiplication")    
print ("d.Division")    
    
choice = input("Type the letter to perform the operation (eg:a for addition) ")    
    
num_1 = int (input ("Enter the first number: "))    
num_2 = int (input ("Enter the second number: "))    
    
if choice == 'a':    
   print (num_1, " + ", num_2, " = ", add(num_1, num_2))    
    
elif choice == 'b':    
   print (num_1, " - ", num_2, " = ", sub(num_1, num_2))    
    
elif choice == 'c':    
   print (num_1, " * ", num_2, " = ", mul(num_1, num_2))    
elif choice == 'd':    
   print (num_1, " / ", num_2, " = ", div(num_1, num_2))    
else:    
   print ("Enter a vaild letter")   
