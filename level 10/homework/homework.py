
str_number = "25"
int_number = int(str_number)
int_age = 30
str_age = str(int_age)
float_value = 10.99
int_value = int(float_value)
is_valid = True
is_older_than_18 = False
age = int(input("type your age: "))
age_in_10_years = age + 10
print(f"age in 10 years: {age_in_10_years}")
age1 = int(input("first person age: "))
age2 = int(input("second person age: "))
age3 = int(input("third person age: "))
num1 = float(input("type first number: "))
num2 = float(input("type second number: "))
sum_result = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2 if num2 != 0 else "გაძლევთ შეცდომას: 0-ით არ შეიძლება გაყრა"
div_num1_by_num2 = num1 // num2
div_num2_by_num1 = num2 // num1

print(f"result: {sum_result}")
print(f"difference: {difference}")


