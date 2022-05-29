# from asyncio import streams


# def counter_string():
#     str=input("Enter the string : ")
     
#     count_upper,count_lower=0

#     for i in str:
#         if i.isupper():
#             count_upper=count_upper+1
#         elif i.islower():
#             count_lower=count_lower+1
#         else:
#             pass

#     print("The number of uppercase is ",count_upper)
#     print("The number of lowercase is ",count_lower)    

# counter_string()

def string_test(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
        if c.isupper():
           d["UPPER_CASE"]+=1
        elif c.islower():
           d["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case Characters : ", d["LOWER_CASE"])

string_test(input("Enter the string : "))
