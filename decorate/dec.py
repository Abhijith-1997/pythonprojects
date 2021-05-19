
def dec_fun(func):
    def wrapper(num1,num2):
        if num1<num2:
            num1,num2=num2,num1
        return func(num1,num2)
    return wrapper
@dec_fun
def div(num1,num2):
    return(num1/num2)
@dec_fun
def sub(num1,num2):
    return(num1-num2)
r=div(10,20)
s=sub(7,6)
print(r)
print(s)