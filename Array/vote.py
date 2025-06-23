voter_age=18
# person_age=input("age=")  not correct because here we are comparing with a string
person_age=int(input("age="))
if person_age>=voter_age:
    print("he/she can vote")
else:
    print("cannot vote")