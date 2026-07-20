print("=" * 50)
print("        DATA TYPE INSPECTOR")
print("=" * 50)

# User Input
name = input("Enter your name: ")
age = input("Enter your age: ")
salary = input("Enter your salary: ")
city = input("Enter your city: ")

print("\n" + "=" * 50)
print("ORIGINAL VALUES")
print("=" * 50)

print("Name   :", name)
print("Age    :", age)
print("Salary :", salary)
print("City   :", city)

print("\n" + "=" * 50)
print("DATA TYPES")
print("=" * 50)

print("Name Type   :", type(name))
print("Age Type    :", type(age))
print("Salary Type :", type(salary))
print("City Type   :", type(city))

print("\n" + "=" * 50)
print("TYPE CONVERSION")
print("=" * 50)

age_int = int(age)
salary_float = float(salary)

print("Age as Integer    :", age_int)
print("Salary as Float   :", salary_float)
print("Age as String     :", str(age_int))
print("Age as Float      :", float(age_int))
print("Salary as Integer :", int(salary_float))
print("Age as Boolean    :", bool(age_int))

print("\n" + "=" * 50)
print("LENGTH FUNCTION")
print("=" * 50)

print("Length of Name :", len(name))
print("Length of City :", len(city))

print("\n" + "=" * 50)
print("RANGE FUNCTION")
print("=" * 50)

start = int(input("Enter the start number: "))
stop = int(input("Enter the stop number: "))
step = int(input("Enter the step value: "))

numbers = list(range(start, stop + 1, step))

print("Numbers :", numbers)
print("Total Numbers :", len(numbers))

print("\n" + "=" * 50)
print("FINAL REPORT")
print("=" * 50)

print("Name           :", name)
print("Age            :", age_int)
print("Salary         :", salary_float)
print("City           :", city)
print("Name Length    :", len(name))
print("City Length    :", len(city))
print("Program Status : Completed Successfully")

print("=" * 50)