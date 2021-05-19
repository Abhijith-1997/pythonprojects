# import re
# x="[abc]" #either a,b or c
# matcher=re.finditer(x,"adbvcx")
# for  match in matcher:
#     print(match.start())
#     print(match.group())
#
#------------------------------

# import re
# x="[^abc]" #except a,b or c
# matcher=re.finditer(x,"adb vcx")
# for  match in matcher:
#     print(match.start())
#     print(match.group())

#--------------------------------

#a to z
# import re
# x="[a-z]"
# matcher=re.finditer(x,"Adbv@$cx")
# for  match in matcher:
#     print(match.start())
#     print(match.group())

#------------------------------------
# not a to z
# import re
# x="[^a-z]"
# matcher=re.finditer(x,"A@dbvcx")
# for  match in matcher:
#     print(match.start())
#     print(match.group())
# #-----------------------------------
 # A to Z
# import re
# x = "[A-Z]"
# matcher = re.finditer(x, "aDA@$dbvcx")
# for match in matcher:
#     print(match.start())
#     print(match.group())

#---------------------------------
#both upper and lower case
# import re
# x = "[a-zA-Z]"
# matcher = re.finditer(x, "aDA@$dbvcx")
# for match in matcher:
#     print(match.start())
#     print(match.group())

#----------------------------------
# 0 to 9 check digits
# import re
# x = "[0-9]"
# matcher = re.finditer(x, "aDA1@$56dbvcx")
# for match in matcher:
#     print(match.start())
#     print(match.group())

#----------------------------
#check special symbol
# import re
# x = "[^a-zA-Z0-9]"
# matcher = re.finditer(x, "aDA@$dbvcx")
# for match in matcher:
#     print(match.start())
#     print(match.group())
#--------------------------------

# check space
# import re
# x = "\s"
# matcher = re.finditer(x, "aDA@ $dbvcx")
# for match in matcher:
#     print(match.start())
#     print(match.group())

#----------------------------------
#check digits
# import re
# x = "\d"
# matcher = re.finditer(x, "aDA@ $4dbvcx")
# for match in matcher:
#     print(match.start())
#     print(match.group())

#----------------------------------------
# except digits
# import re
# x = "\D"
# matcher = re.finditer(x, "aDA@ $4dbvcx")
# for match in matcher:
#     print(match.start())
#     print(match.group())

#----------------------------------------
# all words except digits
# import re
# x = "\w"
# matcher = re.finditer(x, "aDA@ $4dbvcx")
# for match in matcher:
#     print(match.start())
#     print(match.group())

#----------------------------------------
# for a special character
# import re
# x = "\W"
# matcher = re.finditer(x, "aDA@ $4dbvcx")
# for match in matcher:
#     print(match.start())
#     print(match.group())

#------------------------------------------

# quantifiers

# x='a+'        a including group
# x='a'         count including zero number of a
# x='a?'        count a as each including zero no of a
# x='a{2}'      2 no of position
# x='a{2,3}'    minimum 2 a and maximum 3 a
# x='^a'        check starting  with a
# x='a$'        check ending with a




