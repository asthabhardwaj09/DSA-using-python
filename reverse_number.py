def reverse_string(str_reverse):
    rev=""
    for i in str_reverse:
        rev=i+rev
    print(rev)
str_reverse=reverse_string("astha")


def reverseString(s):
  	
    # Reverse the string using slicing
    return s[::-1]


    str = "abdcfe"
    print(reverseString(str))