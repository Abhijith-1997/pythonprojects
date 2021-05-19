# s={1,2,3,4,5,6}
# s1={3,4,1,5}
# for i in s1:
#     if i in s:
#          print(i)

total_stud={"manu","albin","amal","sreerag","bijoy","arun"}
print("total students",total_stud)
failed={"albin","amal","manu"}
print("failed students set",failed)
passed=set()
for i in total_stud:
    if i not in failed:
        passed.add(i)
print("passed students set",passed)
