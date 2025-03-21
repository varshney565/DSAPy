# binStr = input("Enter the binary number")

# n = len(binStr)

# ans = 0
# for i in range(n-1,-1,-1):
#     if binStr[i] == '1': 
#         ans += 2**(n-1-i)


# print(ans) 


#check kth bit is set or not

n = int(input("Enter the number"))
k = int(input("Enter the bit position"))

if n & (1 << k) == 0 :
    print("Bit is not set")
else:
    print("Bit is set")

