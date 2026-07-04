sentence = "learn code learn python code every day"

words = sentence.split()

unique_words = set(words)

print("Unique words:", unique_words)

duplicates_removed = len(words) - len(unique_words)
print("Duplicates removed:", duplicates_removed)