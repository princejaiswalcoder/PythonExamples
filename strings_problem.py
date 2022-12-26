# To Print The Output Separately
name = "Prince"
for i in range(0,len(name)):
    print(name[i])

print("Traversing A String")
f_name = "Prince"
for ch in name:
    print(ch,"#",end='')

print("A Pattern Of Star :")
string = "#"
pattern = ""
for a in range(5): # 0,1,2,3,4
    pattern = pattern + string
    print(pattern)
