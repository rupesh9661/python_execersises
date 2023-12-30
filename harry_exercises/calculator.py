
print("Calculator in python: ")
first_no=(float(input("Enter First Number : ")))

second_no=float(input("Enter Second Number : "))

print("sum of given numbers is : ", first_no+second_no)
print("difference of given numbers is : ", first_no-second_no)
print("product of given numbers is : ", first_no*second_no)
print("quotient of given numbers is : ", first_no/second_no)
if first_no>second_no:
 print("reminder of given numbers is : ", first_no%second_no)
else:
 print("reminder of given numbers is : ", second_no%first_no)


print("floor division of given numbers is : ", first_no//second_no)