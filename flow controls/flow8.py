# 4 subject mark
#total
sub1=int(input("enter ur mark1"))
sub2=int(input("enter ur mark2"))
sub3=int(input("enter ur mark3"))
sub4=int(input("enter ur mark4"))
total=sub1+sub2+sub3+sub4
print(total)
if(180<=total>=200):
    print("grade is A+")
elif(160<=total>=179):
    print("grade is A")
elif(140<=total>=159):
    print("grade is B+")
elif(120<=total>=139):
    print("grade is B ")
elif(100<=total>=119):
    print("grade is c+")
elif(80<=total>=99):
    print("grade is c")
elif(60<=total>=79):
    print("grade is d+")
else:
    print("fail")