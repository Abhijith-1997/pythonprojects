# import re
# n=input("enter")
# x="([a-zA-Z]+\d$)"
# match=re.fullmatch(x,n)
# if match is not None:
#     print("valid")
# else:
#     print("invalid")

# import re
# n=input("enter")
# x="(^a[a-zA-Z0-9\w]*b$)"
# match=re.fullmatch(x,n)
# if match is not None:
#     print("valid")
# else:
#     print("invalid")

# import re
# n=input("enter")
# x="([a-zA-Z]\w{8,15}$\D)"  #([\D]{8,15}$)
# match=re.fullmatch(x,n)
# if match is not None:
#     print("valid")
# else:
#     print("invalid")

# import re
# n=input("enter")
# x="([K][L]\d{2}[A-Z]\d{4}$)"
# match=re.fullmatch(x,n)
# if match is not None:
#     print("valid")
# else:
#     print("invalid")

import re
n=input("enter")
x="([a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-z0-9]+$)"
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")

