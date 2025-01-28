def generate_big_sentence(name, surname, age):
    print("name {}, surname {} and {} age.".format(name, surname, age))
name = input("enter ur age: ")
surname = input("enter ur surname: ")
age = input("enter ur age: ")
generate_big_sentence(name, surname, age)
name = "Nika"
age = 25
print(f"iam {name} and my age {age}")

def my_split(main_string, string_to_split):
    result = main_string.split(string_to_split)
    print(result)
main_string = input("enter main string: ")
string_to_split = input("enter string to split: ")


