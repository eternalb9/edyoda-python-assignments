str=input("  Enter the string : ")
count=0

for i in str:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        count=count+1

print(" The number of vowels is : ",count)
