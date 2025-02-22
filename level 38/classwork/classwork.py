
my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


for i in range(len(my_tuple)):
    print(f"index {i}: {my_tuple[i]}")
def no_duplicates(user_list):
    return list(set(user_list))


list1 = [1, 2, 2, 3, 4, 2, 5]
list2 = ['a', 'b', 'a', 'c', 'z', 'd']
list3 = [10, 20, 30, 20, 40, 50, 7]

print(no_duplicates(list1)) 
print(no_duplicates(list2))
print(no_duplicates(list3))