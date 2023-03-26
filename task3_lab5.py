friends = {
  "Neeraj": "555-1234",
  "Bob": "555-5678",
  "John": "555-9012",
  "Alex": "555-3456"
}
print("Initial dictionary of friends and phone numbers:")
for friend in sorted(friends):
  print(friend + ": " + friends[friend])
name = input("Enter a name to search for: ")
if name not in friends:
  print("Name not found in dictionary. Enter phone number for " + name + ": ")
  phone_number = input()
  friends[name] = phone_number
  print("Updated dictionary:")
else:
  print("Phone number for " + name + ":")
print(friends[name])
