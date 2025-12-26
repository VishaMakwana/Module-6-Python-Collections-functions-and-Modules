# Write a Python program to merge two lists into one dictionary using a loop

key =["name","age","city"]
value=["vishal","20","ahmedabad"]

my ={}

for i in range(len(key)):
    my[key[i]]=value[i]
print(my)    