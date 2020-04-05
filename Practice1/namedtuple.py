from collections import namedtuple
N=int(input())
# ID, MARKS, CLASS and NAME
Student=namedtuple('Student',input().split())
studentList=[]
for i in range(N):
    studentList.append(Student(*input().split()))
#print(studentList)
sum1=0
for i in studentList:
    sum1+=int(i.MARKS)
print(sum1/len(studentList))

