a={}
key=input("enter the key")
words=key.split(" ")
for word in words:
    print(word)
    if word not in a:
        a.update({word:1})
    else:
        val=int(a[word])
        val+=1
        a.update({word:val})
print(a)






