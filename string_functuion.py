name = "prince"
print(len(name),"It Returns Length Of A String")
print(name.capitalize(),"It Capitalize the first letter of a string")
print(name.count("p"),"It returns the occurence of a string")
print(name.find("r"),"It returns the lowest index where the string is found")
print(name.index("c"),"Its same as find() but it returns error when the specified element is not found in the string")
print(name.isalnum(),"Returns TRUE if the character in the string are alphanumeric(Alphabet or Number)")
print(name.isalpha(),"Returns TRUE if the string is alphabet only !")
print(name.isdigit(),"Returns TRUE if the variable contains only digit !")
print(name.isspace(),"Returns TRUE if there are only whitespace")
print(name.islower(),"Returns TRUE if the variable , contains only lowercase alphabet")
print(name.isupper(),"Returns TRUE if variable , contains only UPPERCASE alphabet")
print(name.upper(),"Returns All the string in UPPERCASE !")
print(name.startswith("p"))

print("WAP to input a string and check if it is a palindrome string using a string slice")
s = input("Enter A String : \n")
if s[::-1]:
    print("It's A Plaindrome")
else:
    print("It's Not Palindrome")


s1 = input("Enter A String :\n")
s2 = input("Enter A String2: \n")
if s1 in s2:
    s3 = s2[0:4]+"Restore"
print("Final String :",s1,s3)

print("*".join(name))

string = "#"
pattern = ""
for a in range(5):
    pattern += string
    print(pattern)