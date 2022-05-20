word=input(" Enter the statement : ")
split_word= word.split()
print("The capitalized statement that you wanted is : ")

for i in split_word:
     print(i[0].upper() +i[1:-1] +i[-1].upper(), end=" ")