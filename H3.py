num = int(input("enter a number:"))
if num > 1:
    for i in range(2,num):
        if num % i == 0:
            print(num,"not is check prime number:")
            break
        else:
         print(num, "check prime number:")
else:
 print("The number must be greater than 1:")    
