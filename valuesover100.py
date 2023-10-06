a=int(input("\n Enter limit of list:"))
i=0
lst=[]
while i<a:
    z=int(input("Enter the number"))
    if z>=100:
        lst.append("over listed")
    else:
        lst.append(z)
    i+=1
print(lst)
