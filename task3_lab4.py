def get_name_and_age():
  name = input("Enter your name: ")
  age = int(input("Enter your age: "))
  return name, age


person_name, person_age = get_name_and_age()
print(f"Name: {person_name}")
print(f"Age: {person_age}")
