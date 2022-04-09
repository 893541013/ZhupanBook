a = {"username":"zp","age":"21","sex":"male"}


print(type(a))


v = a["username"]
v1 = a.get("age")
v2 = a.get("username1")
print(v,v1,v2)


a["username"] = "zp1"
print(a) 


del a["age"]
print(a)


a["age"] = 21
print(a)


