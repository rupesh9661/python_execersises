# def sum(a, b):
#     sum=int(a)+int(b)
#     print("sum is",sum)

# a= input()
# b=input()
# sum(a, b)

class School:
     def __init__(self, name, location, students_no):
          print(name+"is a popular convent school located in "+location+" having around ", students_no , "students")

     def fee(self,class_name):
          if class_name=="one":
               print(1000)
          else:
               print(5000) 

class Student(School):
     pass

sobj=Student("royal techno", "bangalore, india", 200)
sobj.fee("two")