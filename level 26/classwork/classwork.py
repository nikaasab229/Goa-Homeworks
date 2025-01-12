def greet(name):
    print(f"გამარჯობა, {name}")
greet("ნიკა")


def manual_range(start, end, step):
    for number in range(start, end, step):
        if number % 2 == 0:
            print(number)
manual_range(1, 10, 1)
manual_range(5, 20, 2)
manual_range(0, 30, 3)
manual_range(10, 50, 5)
manual_range(0, 15, 2)

def manual_len(my_list):
    count = 0  
    for item in my_list:
        count += 1  
    return count
my_list = [1, 2, 3, 4, 5]
print(manual_len(my_list)) 
