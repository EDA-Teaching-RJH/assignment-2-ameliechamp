### Part Four -- your code goes here. 
import random
index = 0
list = []
while index != 10:
    list.append(random.randint(0,100))
    index += 1
print(list)
for i in list:
    while i % 2 != 0:
        list.pop(i)
print(list)