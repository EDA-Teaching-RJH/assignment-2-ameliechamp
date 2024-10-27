### Part Three -- your code goes here.
list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
sorted = list.sort()
for i in list:
    if i == 1:
        list.remove(1)
        list.remove(1) # for some reason only works if two removes are added.
list2 = [7,8]
add = list.append(str(list2)[1:-1])
print(list)
