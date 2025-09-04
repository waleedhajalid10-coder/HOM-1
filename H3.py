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
# num = int(input("أدخل عدد: "))

# if num > 1:  
#     for i in range(2, num):  
#         if num % i == 0:  
#             print(num, "ليس عدداً أولياً")  
#             break  
#     else:  
#         print(num, "عدد أولي")  
# else:  
#     print("العدد يجب أن يكون أكبر من 1")