myList = {
    "name":"👑 Prince Jaiswal",
    "class":11,
    "fav_sub":"💻 computer",
    "subjects":{
      "Economics":"Nice",
      "Computer":"Excellent"
    }
}
myList["class"] = 12
print("Dictionary Are Mutable",myList)
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