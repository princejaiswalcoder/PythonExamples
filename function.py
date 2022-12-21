# Function In Python
# def greeting(greet,name):
#   print(f"Hello {name} , {greet}")

# greeting("Good Morning","Prince")

def tip_calc(food_amt,tip_per):
  tip_amt = food_amt * (tip_per / 100)
  total_amt = food_amt + tip_amt
  print("------------------------")
  print(f"😋 Food Amount {food_amt}")
  print(f"🤑 Tip Amount {tip_per}")
  print("\n")
  print(f"Total Amount {total_amt}")
  print("------------------------")
  return total_amt

# print(tip_calc(100,10))
# OR 
# print(tip_calc(food_amt=100,tip_per=10))



def weather_detect(weather):
  if weather == "rain":
    print("☔")
  elif weather == "cloudy":
    print("🌧")
  else:
    print("🎉")
# weather_detect("lol")

print("Exercises\n")

def bigger_num(a,b):
  if a > b:
    print(a,"Is Bigger")
  else:
    print(b,"Is Bigger")

bigger_num(20,10)