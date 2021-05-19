a=input("enter the string")
vowels="aeiou"
count=0
for i in a:
    if i in vowels:
        count+=1
print(count)
