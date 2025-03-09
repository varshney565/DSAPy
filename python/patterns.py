# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *


# n = int(input("Enter the number of rows "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print("*",end=" ")
#     print()


# *
# * *
# * * *
# * * * *

# n = int(input("Enter the number of rows "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if(j <= i) : 
#             print("*",end = " ")
#         else:
#             print(" ",end = " ")
#     print()



# *   *
#  * * 
#   *  
#  * * 
# *   *



# n = int(input("Enter the number of rows "))
# for i in range(0,n):
#     for j in range(0,n):
#         if i == j or j == n-1-i:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()



#     *    
#    ***   
#   *****  
#  ******* 
# *********


n = int(input("Enter the number of rows "))
m = 2*n-1

for i in range(0,n) :
    for j in range(0,m):
        if j >= n-1-i and j <= n-1+i : 
            print("*",end="")
        else:
            print(" ",end="")
    print()