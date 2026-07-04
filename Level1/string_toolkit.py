sentence = input("Enter a sentence: ")

print("\nUppercase:", sentence.upper())
print("Lowercase:", sentence.lower())
print("Title Case:", sentence.title())

print("Characters:", len(sentence))
print("Words:", len(sentence.split()))

print("Reverse:", sentence[::-1])