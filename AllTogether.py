### Part Four -- your code goes here. 
import random

#create empty list
list = []

#add 10 random numbers to the list
while len(list) < 10:
    list.append(random.randint(0,100))

#iterate through the values in the list
print("\nList values:",end=': ')
for i in list:
    print(i,end=',')

# remove the even numbers
i=0
while i<len(list):
    if (list[i] % 2) == 0:
        list.pop(i)
        #keep index the same
    else:
        # move on to the next element    
        i+=1

#iterate through the new values in the list
print("\nList new values:",end=': ')
for i in list:
    print(i,end=',')