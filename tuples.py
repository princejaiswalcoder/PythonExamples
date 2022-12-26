# 1️⃣ Tuple Are Immutable & it's same as other data type

# Unpacking a tuple:
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

print("Write A Program To Find 2nd Largest Number In A Tuple")
number = eval(input("Enter The Tuple , Ex-(1,2...,n) :"))
sort_asc = sorted(number,reverse=True)
# 👆 it reverse's the entered tuple , in descending order and index it at 1 which is the second largest number
print(sort_asc)
print(sort_asc[1],"Is The Largest 2nd Digit Number")