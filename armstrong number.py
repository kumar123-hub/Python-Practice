number=int(input("Enter a number:"))
original_number=number
sum_of_digits=0
digits_count=len(str(number))
while number>0:
    digit=number%10
    sum_of_digits+=digit**digits_count
    number//=10
if sum_of_digits==original_number:
    print(f"{original_number} is armstrong number")
else:
    print(f"{original_number} is not armstrong number")    