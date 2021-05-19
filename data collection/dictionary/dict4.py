d={1:2,2:3,3:4,4:5,5:6}
def is_key_present(x):
     if x in d:
         print(x,'is present in the dictionary')
     else:
         print(x,'is not present in the dictionary')
ele=input("enter the key")
is_key_present(ele)