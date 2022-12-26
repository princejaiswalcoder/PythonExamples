a = {1,2,3,4,1,2}
# It doesn't print the duplicate items 

# We can't add list inside a set , but we can add tuple because list is mutable and tuple is immutable
print(a)
a.remove(1) # it's used to remove an element
print("Removed Element",a)

s= set()
s.add(20)
s.add(20.0)
s.add("20")
print(s)