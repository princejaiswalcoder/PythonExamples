# Python List Functions

# 1 . Append
print("The append() method adds an item to the end of the list.")
mobile_brand = ["Oppo","Vivo","Poco"]
mobile_brand.append("Music App")
print(mobile_brand)
premium_brand = ["Apple","OnePlus","Samsung"]
premium_brand.append(mobile_brand)
print(f"List Added {premium_brand}")

#2 . Extend
print("Extend Method , it adds list to a list")
mobile_brand = ["Oppo","Vivo","Poco"]
print(mobile_brand)
premium_brand = ["Apple","OnePlus","Samsung"]
premium_brand.extend(mobile_brand)
print(f"List Added {premium_brand}")

# 3. List ()
t1 = ['a','e','u']
insert = t1.insert(2,'i')
print(t1)