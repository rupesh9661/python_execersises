# l1=["rupesh", 22, "delhi", 25000] 
l1=list(("rupesh", 12, "delhi", 25000))
# t1=("rupesh", 22, "delhi", 25000)
t1=tuple(("rupesh", 22, "delhi", 25000))

# s1={"rupesh", 22, "delhi", 25000}
s1=set(("rupesh", 22, "delhi", 25000))
d1={
    "name":"rupesh",
    "age":12,
    "city":"delhi", 
    "salary":25000
}


print(type(l1), type(t1),type(s1),type(d1))

l1.insert(1,"software engineer")
l2=["rup2", 44]
# l1.extend(l2)
# l1.append(l2)
l3=l1+l2
l1.remove("software engineer")
# l1.clear()
print(l1)

for i in l1:
  print(i)

s1.add("software engineer")
s2={"1+", "year", "rupesh"}
# s1.update(s2)
s3=s1.union(s2)
s4=s1.intersection(s2)
# s1.remove("rupesh")
#   s1.discard("rupesh")
# del s1
# s1.clear()
print(s1)
print(s3)
print(s4)

print(d1["name"])
# d1["profile"]="software Engineer"
d1.update({"profile":"software engineer"})
d1.update({"age":21})
# d1.popitem()
# d1.pop("profile")
# d1.clear()
print(d1)
if d1["age"]>=18:
  print("you are eligible for voating")
else:
  print("you are not eligible for voating")  


