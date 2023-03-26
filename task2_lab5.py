usernames_passwords = {
  "user1": "password1",
  "user2": "password2",
  "user3": "password3",
  "user4": "password4",
  "user5": "password5"
}

print("Original dictionary:", usernames_passwords)
usernames_passwords.clear()
print("\nCleared dictionary:", usernames_passwords)

keys = ["user1", "user2", "user3", "user4", "user5"]
default_value = "password"
usernames_passwords = dict.fromkeys(keys, default_value)
print("\nDictionary created with fromkeys():", usernames_passwords)
