# def add(num1,num2):#para1,2
#     return num1+num2
# res=add(9,7)# arg1,2
# print(res)

# error
# def add_three(num1,num2,num3):
#     return num1+num2+num3
# res=add(1,4,5)
# print(res)
# adding many number
# def add(*args):#args(10,20)
#     res=0
#     for num in args:#10
#         res+=num#res=0+10=10+20=30
#     return res
# print(add(10,20))


# def print_employee(**kwars):
#         print(kwars)
# print_employee(id=1000,name="abhi",salary=10000)
employee={
    1000:{"eid":1000,"name":"abhi","salary":25000,"desig":"developer"},
    1001: {"eid": 1001, "name": "arun", "salary": 26000, "desig": "qa"},
    1002: {"eid": 1002, "name": "varun", "salary": 27000, "desig": "ba"},
}
def print_employee(**kwargs):#Kwargs={id:1001,prop:"salary}
    id=kwargs["id"]
    prop=kwargs["prop"]

    if id in employee:
        print(employee[id]["name"])
        print(employee[id]["desig"])

    else:
        print("invalid id")


print_employee(id=1001,prop="desig")



