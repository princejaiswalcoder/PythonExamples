print("Welcome To Love Calculator")
name1 = input("What Is Your Name ? \n")
name2 = input("What Is Their Name ?\n")

# combining the string
combined_string = name1 + name2
lower_case_string = combined_string.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e 

love_score = int(str(true) + str(love))
# love_score = int(love_core)

# Condition

if (love_score < 10) or (love_score > 90):
	print(f"Your Score Is {love_score} , you go together like coke and mentos")
elif (love_score >= 40) and (love_score <= 50):
	print(f"Your Score Is {love_score}, you are alright togather")
else:
	print(f"Your Score Is {love_score}")