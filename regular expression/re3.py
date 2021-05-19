
# import re
# n="helloo9"
# x="\w*"
# match=re.fullmatch(x,n)
# if match is not None:
#     print("valid")
# else:
#     print("invalid")

# import re
# n="56 kg"
# x="\d{2}\s[a-z]{2}"
# match=re.fullmatch(x,n)
# if match is not None:
#     print("valid")
# else:
#     print("invalid")

# import re
# n=input("enter ur number")
# x="[+][9][1]\d{10}"
# match=re.fullmatch(x,n)
# if match is not None:
#     print("valid")
# else:
#     print("invalid")

import re
n=input("enter ur mailid")
x="[a-z]\d{2}[@][gmail][.][com]"
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")