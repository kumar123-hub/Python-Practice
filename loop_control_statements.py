# find the element in the list if element found break 
items=['jam','butter','milk','bread','eggs','cookies','cool drinks']
for item in items:
    if item=='bread':
        print(f'{item} is found')
        break


# #print the first greatest number than 50
# number=int(input('Enter a number: '))
# num=[23,45,6,78,99,67,54]
# for n in num:
#     if n>50:
#         print(f'{n} is greater than 50')
#         break
# else:
#     print('no number is > 50')


# # print whether they login today or not
# todaylog=['developer','tester','designer110','admin001','mana898']
# i=0
# lenght=len(todaylog)
# while i<len(todaylog):
#     if todaylog[i]=='admin001':
#         print(f'{todaylog[i]} is log in today')
#         break 
#     i+=1
# else:
#     print('admin not login')




# # ATM PIN Verification The user gets a maximum of 3 attempts to enter the PIN.
# pin = 5365
# attempts= 0
# while attempts<3:
#     entered_pin=int(input('Enetr a pin: '))

#     if pin == entered_pin:
#         print('correct pin access data')
#         break

#     attempts += 1
#     print(f'invalid pin you have{3-attempts} chances')

# else:
#     print('too many attempts you card blocked')



# #Print only students who passed (marks >= 35)
# #Skip failed students using continue

# students = {
#     'Ravi': 75,
#     'Sita': 28,
#     'Kiran': 65,
#     'Anu': 32,
#     'Rahul': 20
# }
# i=0
# l=list(students.items())
# while i<len(l):
#     if l[i][1]<35:
#         i+=1
#         continue
#     print (l[i])
#     i+=1



# # # Using a for loop, skip employees whose salary is
# # # ₹30,000 or less and print the remaining employees.

# employees = {
#     'Ravi': 25000,
#     'Sita': 40000,
#     'Kiran': 30000,
#     'Anu': 50000
# }
# i=0
# l=list(employees.items())
# while i<len(l):
#     if l[i][1]<=30000:
#         i+=1
#         continue
#     print(l[i][1])
#     i+=1



# #Using a while loop, search through the students and find the first student who failed (marks < 35).


# students = {
#     'Ravi': 75,
#     'Sita': 28,
#     'Kiran': 65,
#     'Anu': 32,
#     'Rahul': 20
# }
# i = 0
# l = list(students.items())
# while i < len(l):
#     if l[i][1] < 35:
#         print(f'The failed student is: {l[i]}')
#         break
#     i += 1

# #Shopping Cart Budget Checker
# budget = int(input("Enter your budget: "))
# n = int(input("Enter number of products: "))
# total = 0
# i = 0
# while i < n:
#     price = int(input(f"Enter price of product {i + 1}: "))
#     if price <= 0:
#         print("Invalid price! Skipping...")
#         i += 1
#         continue
#     total += price
#     if total > budget:
#         print("Budget exceeded!")
#         break
#     i += 1
# else:
#     print("All products processed successfully.")
# print("Total amount:", total)


