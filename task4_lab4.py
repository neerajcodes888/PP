sentence = input("Enter a sentence: ")
words = sorted(sentence.split(), key=lambda x: len(x), reverse=True)
print("Sorted words in decreasing order of length:")
for word in words:
  print(f"{word}: {len(word)}")
