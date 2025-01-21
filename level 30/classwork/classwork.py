
name = input("please, enter your choice: ")
choice = input("please, enter your choice ('u' - uppercase ან 'l' - lowercase): ")
if choice == 'u':
    print(name.upper())  
elif choice == 'l':
    print(name.lower()) 
else:
    print("wrong information")

def manual_find(main_string, str_to_find):

    for i in range(len(main_string) - len(str_to_find) + 1):

        if main_string[i:i + len(str_to_find)] == str_to_find:
            return i
    return -1
print(manual_find("hello world", "world"))  # Output: 6
print(manual_find("hello world", "python")) # Output: -1


main_str = input("გთხოვთ, შეიტანოთ მთავარი სთრინგი: ")
str_to_count = input("გთხოვთ, შეიტანოთ დასათვლელი სთრინგი: ")
count = main_str.count(str_to_count)
print(count)
def manual_swapcase(input_string):
    swapped_string = ""
    
    
    for char in input_string:
        if char.islower(): 
            swapped_string += char.upper() 
        elif char.isupper():  
            swapped_string += char.lower()  
        else:
            swapped_string += char  
    
    return swapped_string


print(manual_swapcase("Hello World!"))  # Output: hELLO wORLD!
print(manual_swapcase("Python123"))     # Output: pYTHON123
