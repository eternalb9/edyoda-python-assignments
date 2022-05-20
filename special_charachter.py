


str = input("Enter a string : ")

length=len(str)
for i in range(length-1):
    if str[i].isalnum()==1 or str[i].isspace()==1:
        i=i+1
        

    else:
        print(" The string is not acceptable.")
           

if i==length-1:
    print("The string is acceptable")
