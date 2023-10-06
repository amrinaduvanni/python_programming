a=input("Enter sentence\n")
b=input("\nEnter the word to search\n")
list=a.split()
count=0
for w in list:
    if w==b:
        count=count+1
print("count:",count)
