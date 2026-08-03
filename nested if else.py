 # Nested if-else is used to check multiple related conditions by placing one if-else statement inside another if or else block.

 # 1.program to check order placed or not based on card number and cv using nedted 


card=int(input('enter your card number: '))
card1=564564
cv=int(input('enter your cv '))
cv1=563
if card==card1 and cv==cv1:
    otp=int(input('enter your otp: '))
    myotp=1234
    if otp==myotp:
        print("order placed")
    else:
        print('order not placed')
else:
    print('invalid card details')

# 2.  chceck eligibility or not for promotion and salary hike based on the performance

# experience=int(input('enter your  experience: '))
# if experience>3:
#     performence=input('you have best performence or not: ')
#     if performence=='yes':
#         print('you are eligible for prootion')
#     elif performence=='good':
#         print("'you are eligible for salary hike")
#     else:
#         print('improve your perfromance')
# else:
#     print('do not have any experience')



# 3.student can write exams or not based on the fees and attendence 


# fees=(input("do you pay fees: "))
# if fees=='yes':
#     attendence=int(input("Enter your attendence: "))
#     if attendence>75:
#         print("you cannot pay condonation and ready for exams")
#     else:
#         print("you pay condonation and ready for exam")
# else:
#     print("you cannot write exam")



# \4. check a person can drive a bike or anything based on the conditions like age,license using nested if
    

# age=int(input("Enter your age: "))
# if age>18:
#     license=input("do you have license: ")
#     license=='yes'
#     if license=='yes':
#         print("you can drive")
#     else:
#         print("need license to drive")
# else:
#     print('minors cannot drive ')    