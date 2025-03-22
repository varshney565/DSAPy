# binStr = input("Enter the binary number")

# n = len(binStr)

# ans = 0
# for i in range(n-1,-1,-1):
#     if binStr[i] == '1': 
#         ans += 2**(n-1-i)


# print(ans) 


#check kth bit is set or not

# n = int(input("Enter the number"))
# k = int(input("Enter the bit position"))

# if n & (1 << k) == 0 :
#     print("Bit is not set")
# else:
#     print("Bit is set")



# count the number of set bits
# n = int(input("Enter the number"))

# ans = 0
# while n > 0 : 
#     if n&1 == 1:
#         ans += 1
#     n = n >> 1

# print(ans)





input = [2,2,5,5,1,1,9,9,9,8,8]

res = 0

for i in range(0,len(input)):
    res = res^input[i]

print(res)