a = int(input("enter the first number : "))

b = int(input("enter the second number : "))

c = int(input("enter the third number : "))

# if a > b : 
#     print("Maximum number is : ",a)
# else :
#     print("Maximum number is : ",b)


if a > b : 
    if a > c : 
        print("Maximum number is : ",a)
    else : 
        print("Maximum number is : ",c)
else : 
    if b > c :
        print("Maximum number is : ",b)
    else : 
        print("Maximum number is : ",c)