myList = {
    "name":"👑 Prince Jaiswal",
    "class":11,
    "fav_sub":"💻 computer",
    "subjects":{
      "Economics":"Nice",
      "Computer":"Excellent"
    }
}
# Characteristics Of Dicitionary
# 1. It's Unordered Set
# 2. Not A Sequence
# 3. Indexed By Key ,Not Numbers
# 4. Keys Must Be Unique
# 5. Dictionaries Are Mutable

myList["class"] = 12
# print("Dictionary Are Mutable",myList)
updateDict = {
    "Telegram":"Telegram Bot Lover",
    "Fan":"Me Fan Of Coding"
}
# Dictionay Methods 👇
# print(list(myList.keys()))
# Prints The Keys Of The Element 👇
# print(list(myList.values()))
# This Is Used To Push The Values Inside A List 👇
# myList.update(updateDict)
# print("Added Dictionary Items",myList)

# print(myList.get("name")) 
# This Is Use To Get The Value Of Particular Element In Dictionary 👆
# print(myList["name"])
# Both Method Are Same , But Difference Is That , .get() method return 'none' , when element is not found , and 
# indexing menthod return error when an element is not found 

# 😋 Write a program to read roll numbers and marks of four students and create a dictionary from it having roll numbers as keys ❓

# 👇 Answer 🤯
# roll = []
# marks = []
# for a in range(4):
#   r,m = eval(input("Enter Roll Number 🧑 & Marks 📑 :\n"))
#   roll.append(r)
#   marks.append(m)
# d = {
#   roll[0]:marks[0],
#   roll[1]:marks[1],
#   roll[2]:marks[2],
#   roll[3]:marks[3],
# }
# print(f"Created Dictionary {d}")

# M = {}
# n = int(input("How Many Students ?"))
# for a in range(n):
#   r,m = eval(input("Enter Roll No. & Marks :"))
#   M[r] = m # it works like this
   #M is dictionary , r is key and m is value
   # <dictionary>[key] = <value>
# print(f"Created Dictionary {M}")

# Write a program to print a dictionary that share a common value with all the keys
# keys_ex = dict.fromkeys([10,20,30],"Prince")
# fromkeys is a fucntion , PRINCE acts as a value and shares it will all the keys
# print(keys_ex)

