friends_dict = {
  "Neeraj": "123-456-7890",
  "Bob": "456-789-1230",
  "Alex": "789-123-4560",
  "David": "321-654-0987",
}
sorted_friends_dict = dict(sorted(friends_dict.items()))

print("Friends Dictionary:")
for friend, phone in sorted_friends_dict.items():
  print(f"{friend}: {phone}")

name = input("Enter a friend's name: ")

if name in sorted_friends_dict:
  print(f"{name}'s phone number is {sorted_friends_dict[name]}")
else:

  phone = input("Enter phone number for " + name + ": ")
  sorted_friends_dict[name] = phone
  print(f"{name}'s phone number ({phone}) has been added to the dictionary.")

print("Updated Friends Dictionary:")
for friend, phone in sorted_friends_dict.items():
  print(f"{friend}: {phone}")
