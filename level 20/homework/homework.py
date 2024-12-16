num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))


if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3


print("The largest number is:", largest)







def get_score(): 
    score = float(input("type score (0-100): ")) 
    return score  
def determine_grade(score): 
    if 90 <= score <= 100: 
        return "A" 
    elif 80 <= score < 90: return "B" 
    elif 70 <= score < 80: 
        return "C" 
    elif 60 <= score < 70: return "D" 
    else: 
        return "F"  
if __name__ == "__main__": 
    score = get_score() 
    grade = determine_grade(score) 
    print("grade:", grade)



number = float(input("enter number: "))   
if number > 0: 
    print("number is positive") 
elif number < 0: 
    print("number is negative") 
else: 
    print("number is zero")




start = int(input("type first number: ")) 
end = int(input("type second number: ")) 
total_sum = 0 
for num in range(start, end + 1): 
    total_sum += num  
print("total sum {} {} : {}".format(start, end, total_sum))



number = int(input("type number: "))  
def is_prime(num): 
    if num <= 1: 
        return False 
    for i in range(2, int(num ** 0.5) + 1): 
        if num % i == 0: return False 
        return True  
    if is_prime(number): 
        print(f"{number} easy number") 
    else: 
        print(f"{number} is not easy number")



numbers = [10, 20, 30, 40, 50]  
print("first element:", numbers[0])
print("third element:", numbers[2]) 
print("last element", numbers[-1])



elements = [10, "orange", 3.14, True, [1, 2, 3], {"key": "value"}, (4, 5), None, "banana", 99, 
            7.77, "hello", False, 2023, [4, 5, 6], {"another_key": "another_value"}, (6, 7), 
            "grape", 0, -123]  
for i in range(len(elements)): 
    print(f"element {i}: {elements[i]}")