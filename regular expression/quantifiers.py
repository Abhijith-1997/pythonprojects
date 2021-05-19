# quantifiers

# x='a+'        a including group
# x='a*'         count including zero number of a
# x='a?'        count a as each including zero no of a
# x='a{2}'      2 no of position
# x='a{2,3}'    minimum 2 a and maximum 3 a
# x='^a'        check starting  with a
# x='a$'        check ending with a

#------------------------------------------
# import re
# x="a+"  # a including group
# r="aaa as a chka"
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())

#-----------------------------------------
# count including zero number of a
# import re
# x="a*"
# r="aaa as a chka"
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())
#---------------------------------------------------
# count a as each including zero number of a
# import re
# x="a?"
# r="aaa as a chka"
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())
#----------------------------------------
#  number of position
# import re
# x="a{2}"
# r="aaa as aa chka"
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())
#-------------------------------------------
# minimum 2 a and maximum 3a
# import re
# x="a{2,3}"
# r="aaa as aaa aa chka"
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start(),":",match.group())

#---------------------------------------------
#check staring with a
# import re
# x="^a"
# r="aa as aa chka"
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start(),":",match.group())

# import re
# x="^a"
# r="gaaa as aa chka"
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start(),":",match.group())
#------------------------------------------------------
#ending with a
# import re
# x="a$"
# r="aa as aa hka"
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start(),":",match.group())
#
#----------------------------------------------------




