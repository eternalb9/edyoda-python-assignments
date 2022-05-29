def add_list():
    sum = 0
    size=int(input("  Enter the size of the list : "))
    lst = []
    for i in range(size):
        data=int(input(" Enter the element you want to get added : "))
        lst.append(data)

    for i in lst:
        sum = sum + i

    return sum    

result=add_list()
print("The addition of your elements is : ",result)