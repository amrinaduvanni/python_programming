d={'a':1,'b':2,'c':3,'d':4}
print("intitial dictionary")
print(d)
key=input("enter the key delete(a-d):")
if key in d:
    del d[key]
else:
    print("key not found  !")
    exit(0)
print("updated dictionary")
print(d)
    
