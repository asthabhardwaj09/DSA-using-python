# user= 123
# o/p 1+2+3


# user_num=input("enter the num: ")#123
# for i in range(len(user_num)):
#     print(i)

user_num = input("Enter a number: ")  # input as string, e.g., "123"
total = 0

for digit in user_num:
    total=total+ int(digit)

print("Sum of digits =", total)
print(type(total))


a=input("enter a number")
a=(int(a))
print(a+1)
print(type(a))


#################################

user_num = input("Enter a number: ")  # e.g. "123"
total = 0

for i in range(len(user_num)):
    total = total + int(user_num[i])  # using index to access each digit

print("Sum of digits =", total)
print(type(total))

    
