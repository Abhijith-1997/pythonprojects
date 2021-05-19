lst=[12,33,4,2,44,5,66,7,88]
def bsearch():
    lst.sort()
    print(lst)
    ele=int(input("enter the element"))
    fla=0
    low=0
    up=len(lst)-1
    while low<=up:
        mid=(low+up)//2
        if ele>lst[mid]:
            low=mid+1
        elif ele<lst[mid]:
            up=mid-1
        elif ele==lst[mid]:
            fla=1
            break
    if fla==1:
        print("found")
    else:
        print("not found")
bsearch()