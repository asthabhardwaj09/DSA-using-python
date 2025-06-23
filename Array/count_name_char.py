# astha
# a=2
# s=1
# t=1
# h=1

# count=0
# name="astha"
# if "a" in name:
#     count=count+1
#     print(count)

# it will not tell how many time because it only tell the presence of a is there or not



# name = "astha"
# for ch in name:
#     print(ch, "=", name.count(ch))

# name="astha"
# checked=""
# for i in name:
#     if i not in checked:
#         count =0
#         for j in name:
#             if i==j:
#                 count=count+1
#         print(f"{i}={count}")
#         checked=checked+i
#     else:
#         pass


# user_name=input("enter your name: ") #ravita
# checked=""
# for i in user_name:
#     if i not in checked:
#         count=0
#         for j in user_name:
#             if i==j:
#                 count=count+1
#         print(f"{i}={count}")
#         checked=checked+i


# user_name=input("enter your name: ") #ravita
# checked=""
# for i in range(len(user_name)):
#     print(i) #why not to apply this method
#     if i not in checked:
#         count=0
#         for j in user_name:
#             if i==j:
#                 count=count+1
#         print(f"{i}={count}")
#         checked=checked+i

user_name = input("Enter your name: ")  # e.g. ravita
checked = ""

for i in range(len(user_name)):
    # print(user_name[i])
    if user_name[i] not in checked:      # check character, not index
        count = 0
        for j in user_name:
            if user_name[i] == j:
                count += 1
        print(f"{user_name[i]} = {count}")
        checked = checked + user_name[i]  # add character to checked



# checked = checked + i is important to remember which characters have already been counted — without it, duplicate counts will show.

# print(user_name[i])
a="astha"
print(a[1])



