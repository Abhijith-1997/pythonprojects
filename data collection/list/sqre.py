# list comprehensions are used for creating new lists from other iterables.
# as list comprehensions return lists,they consist of brackets containing the expression,
# which is executed for each element along with the forloop to iterative over each element
# a=[2,3,4,5,6]
# b=[]
# for i in a:
#     b.append(i*i)
# print(a)
# print(b)

numbers=[1,2,3,4]
squares=[n**2 for n in numbers]
print(squares)